import os
import json
import uuid
from mockingbird.repository.dynamo_repository import DynamoRepository
from mockingbird.utils.logger import get_logger
from mockingbird.schemas.stub import STUB_OBJECT
from mockingbird.utils.consts import STUBS_TABLE

DYNAMODB = os.environ.get("DYNAMO_URL")


def validate_stub(stub_params):
    from jsonschema import validate
    validate(stub_params, STUB_OBJECT)


def create_stub(event):
    log = get_logger("create_stub")
    log.info("Creating stub with params %s" % json.dumps(event))

    new_stubb = {
        "Id": str(uuid.uuid4()),
        "Namespace": "random",
        "Stubb": event
    }

    repo = DynamoRepository(DYNAMODB)
    response = repo.store_stub(table_name=STUBS_TABLE, item=new_stubb)
    metadata = response.get("ResponseMetadata")

    if metadata.get("HTTPStatusCode") != 200:
        raise Exception("Error storing stub in dynamo")

    created_stub = repo.get_stubs(table_name=STUBS_TABLE, id=new_stubb["id"])
    return created_stub


def delete_stub(stub_id: str, pattern: str):
    pass


def get_all_stubs():
    repo = DynamoRepository(DYNAMODB)
    stubs = repo.get_stubs(table_name=STUBS_TABLE)
    return { "items": stubs }
