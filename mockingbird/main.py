import json
from mockingbird.services import stub_manager


def mock_it(event: dict, context):
    # this path file will contain the requested path
    path = event.get("path")
    method = event.get("httpMethod")  # http method used in the call
    body = event.get("body")
    headers = event.get("headers")

    print("% %s", path, method)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
