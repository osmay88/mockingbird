import json
import re

from mockingbird.services import stub_manager
from mockingbird.utils import extract_namespace_from_url


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
            return stub["stub"]["response"]

    return json.dumps(stubs)
