from pytest_mock import MockerFixture

from mockingbird.routes.mock_it import mock_it


def test_path_params_missing(mocker: MockerFixture):
    request = {
        "body": None,
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Host": "127.0.0.1:3000",
            "X-Forwarded-Port": "3000",
            "X-Forwarded-Proto": "http"
        },
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "multiValueQueryStringParameters": None,
        "path": "/mock-it/some/thing/hey",
    }

    response = mock_it(request)
    assert response.get("statusCode"), 400
    assert response.get("body"), '{"error": "pathParameters is missing"}'


def test_event_path_is_missing_or_empty(mocker: MockerFixture):
    request = {
        "body": None,
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Host": "127.0.0.1:3000",
            "Postman-Token": "455c2fa0-07f6-470b-be6c-9cfc3bef98c1",
            "User-Agent": "PostmanRuntime/7.26.8",
            "X-Forwarded-Port": "3000",
            "X-Forwarded-Proto": "http"
        },
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "path": "/mock-it/some/thing/hey",
        "pathParameters": {
            "event": ""
        },
    }

    response = mock_it(request)
    assert response["statusCode"] == 400, "Should trigger a bad request response"
    assert response["body"] == '{"error": "event path missing or empty"}', "should contain the error message in payload"

