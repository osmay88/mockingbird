import json
from http import HTTPStatus

from mockingbird.services import request_manager
from mockingbird.utils.aws_utils import make_response
from mockingbird.utils.exc import MockingException
from mockingbird.utils.logger import get_logger


def mock_it(event: dict, context=None):
    """
    This is the endpoint handling the mock requests
    """
    log = get_logger("mock_it_route")
    log.debug("Received event %s" % json.dumps(event))
    path_params: dict = event.get("pathParameters")
    if not path_params:
        return make_response(HTTPStatus.BAD_REQUEST, error="pathParameters is missing")

    path_event: str = path_params.get("event")
    if not path_event or path_event == "":
        return make_response(HTTPStatus.BAD_REQUEST, error="event path missing or empty")

    if not path_event.startswith("/"):
        path_event = "/" + path_event

    method = event.get("httpMethod")
    body = event.get("body")
    headers = event.get("headers")

    try:
        return request_manager.handle_request(path_event, method, headers, body)
    except MockingException as err:
        log.error("an exception has occur while handling a request %s" % err)
        return make_response(err.error_code, error=err.msg)
    except Exception as err:
        return make_response(500, str(err))
