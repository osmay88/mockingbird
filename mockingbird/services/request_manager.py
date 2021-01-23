import json

from mockingbird.services import stub_manager
from mockingbird.utils import extract_namespace_from_url


def handle_request(path: str, method: str, headers: dict, body: dict) -> str:
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
    return json.dumps(stubs)
