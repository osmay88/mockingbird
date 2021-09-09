import json
import re

from mockingbird.services import stub_manager
from mockingbird.services.templating_manager import render_template
from mockingbird.utils import extract_namespace_from_url
from mockingbird.utils.exc import MockingException
from mockingbird.utils.logger import get_logger


def build_response(stub_item: dict):
    response_obj = stub_item.get("response")
    response = {
        "statusCode": response_obj["status"],
        "body": render_template(response_obj["body"]),
        "headers": response_obj["headers"]
    }
    return response


def validate_request_params(stub, method, headers):
    request_obj = stub.get("request")
    request_method = request_obj.get("method")
    if request_method != "ANY" and request_obj.get("method") != method:
        raise MockingException("The request method doesn't match stub",
                               error_code=400, http_status_code=400)


def handle_request(path: str, method: str, headers: dict, body: dict):
    """
    Processes an incoming request and return the string body
    if the mock doesn't exist we return an exception
    :param path:
    :param method:
    :param headers:
    :param body:
    :return:
    """
    log = get_logger("handle_request_service")

    namespace = extract_namespace_from_url(path)

    stubs = stub_manager.get_stub(namespace=namespace) # get all the urls for that namespace

    for stub in stubs["items"]:
        url_pattern = stub["stub"]["request"]["url"]
        exp = re.compile(url_pattern)
        if exp.match(path):
            validate_request_params(stub["stub"], method, headers)
            return build_response(stub["stub"])

    raise MockingException(error_code=404,
                           http_status_code=404,
                           msg="No stub with for the path %s found" % path)
