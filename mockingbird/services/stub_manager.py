import json
import uuid

from mockingbird.repository.repository import Repository
from mockingbird.schemas.stub import STUB_OBJECT
from mockingbird.utils import hash_url, extract_namespace_from_url
from mockingbird.utils.exc import MockingException
from mockingbird.utils.logger import get_logger


def validate_existing_url(url: str):
    repo = Repository.get_repository()
    hashed_url = hash_url(url)
    result = repo.get_url_hash(hashed_url)
    if len(result):
        raise MockingException(msg="An stub already exist using the same url pattern, stub id: %s" % result[0]["stub_id"], error_code=400)


def validate_stub_schema(stub):
    from jsonschema import validate
    from jsonschema import ValidationError
    try:
        return validate(stub, STUB_OBJECT)
    except ValidationError as err:
        raise MockingException(msg="The schema validation for the stub failed with error: %s" % err.message, error_code=400)


def validate_stub(stub_params):
    """
    Validates is a stub structure is correct.
    validates that the stub schema is correct.
    :param stub_params:
    """

    # Validates that the stub schema is correctly formatted
    # when running from SAM local, comment this line
    validate_stub_schema(stub_params)

    request = stub_params.get("request")
    if not request:
        raise MockingException(msg="request object missing in stub", error_code=500)

    validate_existing_url(request["url"])


def create_stub(event):
    """
    Creates a new stub object and stores it into the database.
    """

    def store_stub(repo, item):
        new_stub = {
            "id": str(uuid.uuid4()),
            "namespace": extract_namespace_from_url(item["request"]["url"]),
            "stub": item
        }
        log.info("Storing stub %s" % json.dumps(new_stub))
        response = repo.store_stub(item=new_stub)
        metadata = response.get("ResponseMetadata")

        if metadata.get("HTTPStatusCode") != 200:
            raise Exception("Error storing stub in dynamo")
        return new_stub

    def store_url_hash(repo, item):
        url_hash = {
            "url_hash": hash_url(event["request"]["url"]),
            "stub_id": item["id"]
        }
        hash_response = repo.store_url_hash(url_hash)
        hash_metadata = hash_response.get("ResponseMetadata")
        if hash_metadata.get("HTTPStatusCode") != 200:
            log.info("Http error code %s" % hash_metadata.get("HTTPStatusCode"))
            raise Exception("Error storing url hash in dynamo")

    log = get_logger("create_stub")
    log.info("Creating stub with params %s" % json.dumps(event))
    validate_stub(event)
    repository = Repository.get_repository()
    created_stub = store_stub(repository, event)
    store_url_hash(repository, created_stub)
    return created_stub


def delete_stub(stub_id: str, pattern: str):
    pass


def get_stub(stub_id=None, namespace=None):
    try:
        repo = Repository.get_repository()
        stubs = repo.get_stubs(stub_id=stub_id, namespace=namespace)
        return {"items": stubs}
    except Exception as err:
        raise MockingException(msg=str(err), error_code=500)
