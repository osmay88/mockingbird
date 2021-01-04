import os
import json
import uuid
from mockingbird.repository.dynamo_repository import DynamoRepository
from mockingbird.utils.logger import get_logger
from mockingbird.schemas.stub import STUB_OBJECT
from mockingbird.utils.consts import STUBS_TABLE, URL_HASH_TABLE


DYNAMODB = os.environ.get("DYNAMO_URL")



def hash_url(url: str):
    from hashlib import sha1
    hash = sha1(url.encode())
    return hash.hexdigest()


def validate_stub(stub_params):
    def validate_existing_url(url: str):
        repo = DynamoRepository(DYNAMODB)
        hashed_url = hash_url(url)
        result = repo.get_url_hash(URL_HASH_TABLE, hashed_url)
        if len(result):
            raise Exception("An stub already exist using the same url pattern, stub id: %s" % result[0]["stub_id"])

    request = stub_params.get("request")
    if not request:
        raise Exception("request object missing in stub")

    validate_existing_url(request["url"])


def create_stub(event):

    def store_stub(repo, item):
        new_stub = {
            "id": str(uuid.uuid4()),
            "namespace": "random",
            "stub": item
        }
        log.info("Storing stub %s" % json.dumps(new_stub))
        response = repo.store_stub(table_name=STUBS_TABLE, item=new_stub)
        metadata = response.get("ResponseMetadata")

        if metadata.get("HTTPStatusCode") != 200:
            raise Exception("Error storing stub in dynamo")
        return new_stub

    def store_url_hash(repo, item):
        url_hash = {
            "url_hash": hash_url(event["request"]["url"]),
            "stub_id": item["id"]
        }
        hash_reponse = repo.store_url_hash(URL_HASH_TABLE, url_hash)
        hash_metadata = hash_reponse.get("ResponseMetadata")
        if hash_metadata.get("HTTPStatusCode") != 200:
            log.info("Http error code %s" % hash_metadata.get("HTTPStatusCode"))
            raise Exception("Error storing url hash in dynamo")

    log = get_logger("create_stub")
    log.info("Creating stub with params %s" % json.dumps(event))
    validate_stub(event)
    repo = DynamoRepository(DYNAMODB)
    new_stub = store_stub(repo, event)
    store_url_hash(repo, new_stub)

    
    created_stub = repo.get_stubs(table_name=STUBS_TABLE, id=new_stub["id"])
    return created_stub


def delete_stub(stub_id: str, pattern: str):
    pass


def get_all_stubs():
    repo = DynamoRepository(DYNAMODB)
    stubs = repo.get_stubs(table_name=STUBS_TABLE)
    return {"items": stubs}
