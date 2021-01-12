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
    print(body)
    if not body:
        return make_response(HTTPStatus.BAD_REQUEST, "Missing request body")
    data = json.loads(body)
    log.info("stub to create %s" % json.dumps(data))
    try:
        response = stub_manager.create_stub(data)
        log.info("Created stub %s" % response)
        return make_response(HTTPStatus.CREATED,
                             json.dumps(response, csl=DecimalEncoder))
    except Exception as err:
        print(err)
        return make_response(HTTPStatus.BAD_REQUEST, json.dumps(str(err)))


def get_all_stubs(event, context):
    """
    returns all the stubs in the db
    """
    log = get_logger("get_stub_route")
    path_params = event.get("pathParameters", dict())
    log.info("Received params %s", json.dumps(path_params))
    stubs = stub_manager.get_stubs(id=path_params.get("stub_id"))
    return make_response(HTTPStatus.OK, json.dumps(stubs, cls=DecimalEncoder))
