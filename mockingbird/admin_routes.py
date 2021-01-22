import json
from http import HTTPStatus
from mockingbird.services import stub_manager
from mockingbird.utils.logger import get_logger
from mockingbird.utils.decimal_encoder import DecimalEncoder
from mockingbird.utils.aws_utils import make_response


def create_stub(event: dict, context):
    """
    Stores a new stub in the database.
    """
    log = get_logger("create_stub_route")

    body = event.get("body")
    if not body:
        return make_response(HTTPStatus.BAD_REQUEST, error="Missing request body")
    data = json.loads(body)
    log.info("stub to create %s" % json.dumps(data))
    try:
        response = stub_manager.create_stub(data)
        log.info("Created stub %s" % response)
        return make_response(HTTPStatus.CREATED,
                             json.dumps(response, cls=DecimalEncoder))
    except Exception as err:
        log.error("an exception has occur while creating the stub %s" % err)
        return make_response(HTTPStatus.BAD_REQUEST, error=str(err))


def get_stub(event, context):
    """
    returns all the stubs in the db
    """
    log = get_logger("get_stub_route")
    path_params = event.get("pathParameters")
    stub_id = None
    if path_params:
        log.info("Received params %s", json.dumps(path_params))
        stub_id = path_params.get("stub_id")
    stubs = stub_manager.get_stub(stub_id)
    return make_response(HTTPStatus.OK, json.dumps(stubs, cls=DecimalEncoder))
