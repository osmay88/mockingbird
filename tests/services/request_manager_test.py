from uuid import uuid4

from pytest_mock import MockerFixture

from mockingbird.services.request_manager import handle_request


def test_proper_url_is_find(mocker: MockerFixture):
    text = "This is a text %s" % uuid4().hex
    status_code = 200
    custom_header = uuid4().hex

    def mock_get_stub(*args, **kwargs):
        stub_body = {
            "request": {
                "method": "GET",
                "url": "/namespace/thing"
            },
            "response": {
                "status": status_code,
                "body": text,
                "headers": {
                    "Content-Type": "text/plain",
                    "Custom-Header": custom_header
                }
            }
        }

        return {
            "items": [
                {"stub": stub_body}
            ]
        }
    mocker.patch(
        "mockingbird.services.stub_manager.get_stub",
        mock_get_stub
    )

    response = handle_request("/namespace/thing", "GET", dict(), dict())
    assert response["body"] == text, "The text should match the original"
    assert response["statusCode"] == status_code, "The status code should match the stub one"
    assert "Custom-Header" in response["headers"].keys(), "The proper header should be set"
    assert response["headers"]["Custom-Header"] == custom_header, "The header value must be correct"
