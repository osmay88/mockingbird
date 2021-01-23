import json

from mockingbird.services import request_manager
from mockingbird.utils.aws_utils import make_response


def mock_it(event: dict, context):
    # this path file will contain the requested path
    pathParams = event.get("pathParameters")
    path = "/" + pathParams.get("event")
    print(json.dumps(event))
    method = event.get("httpMethod")  # http method used in the call
    body = event.get("body")
    headers = event.get("headers")

    print("% %s", path, method)
    try:
        result = request_manager.handle_request(path, method, headers, body)
        return {
            'statusCode': 200,
            'body': result
        }
    except Exception as err:
        return make_response(500, str(err))
