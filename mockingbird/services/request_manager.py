from mockingbird.services import stub_manager


def handle_request(request, *args, **kwargs):
    """
    Processes an incoming request and return the string body
    if the mock doesn't exist we return an exception
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    return ""