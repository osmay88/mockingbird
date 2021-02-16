import json
from http import HTTPStatus

from mockingbird.services import request_manager
from mockingbird.utils.aws_utils import make_response
from mockingbird.utils.logger import get_logger


def mock_it(event: dict, context=None):
    # this path file will contain the requested path
    log = get_logger("mock_it_route")
    path_params = event.get("pathParameters")
    if not path_params:
        return make_response(HTTPStatus.BAD_REQUEST, error="pathParameters is missing")

    path_event: str = path_params.get("event")
    if not path_event or path_event == "":
        return make_response(HTTPStatus.BAD_REQUEST, error="event path missing or empty")

    if not path_event.startswith("/"):
        path_event = "/" + path_event

    log.debug(json.dumps(event))
    method = event.get("httpMethod")  # http method used in the call
    body = event.get("body")
    headers = event.get("headers")

    log.debug("% %s", path_event, method)
    try:
        result = request_manager.handle_request(path_event, method, headers, body)
        return {
            'statusCode': 200,
            'body': result
        }
    except Exception as err:
        return make_response(500, str(err))
