import json
import re

from mockingbird.services import stub_manager
from mockingbird.utils import extract_namespace_from_url
from mockingbird.utils.exc import MockingException


def build_response(stub_item: dict):
    response_obj = stub_item.get("response")
    response = {
        "statusCode": response_obj["status"],
        "body": response_obj["body"],
        "headers": response_obj["headers"]
    }
    return response


def validate_request_params(method, headers):
    pass


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
    namespace = extract_namespace_from_url(path)
    stubs = stub_manager.get_stub(namespace=namespace)
    for stub in stubs["items"]:
        url_pattern = stub["stub"]["request"]["url"]
        exp = re.compile(url_pattern)
        if exp.match(path):
            validate_request_params(method, headers)
            return build_response(stub["stub"])

    raise MockingException(error_code=404,
                           http_status_code=404,
                           msg="No stub with for the path %s found" % path)
