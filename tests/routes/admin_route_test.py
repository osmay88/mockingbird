import json

from pytest_mock import MockerFixture

from mockingbird.admin_routes import create_stub
from tests import *


def test_admin_create_stub(mocker: MockerFixture):
    stub_body = {
        "request": {
            "method": "GET",
            "url": "/some/thing"
        },
        "response": {
            "status": 200,
            "body": "Hello world!",
            "headers": {
                "Content-Type": "text/plain"
            }
        }
    }

    new_stub_request = {
        "body": json.dumps(stub_body)
    }

    def create_mock(*args, **kwargs):
        stub_body["id"] = "hahahahahahaha"
        return {
                "id": "hahahahhahaha",
                "namespace": "random",
                "stub": stub_body
            }

    mocker.patch(
        "mockingbird.services.stub_manager.create_stub",
        create_mock
    )

    response = create_stub(new_stub_request, None)
    assert response.get("body") is not None
    body = json.loads(response.get("body"))
    stub = body.get("stub")
    assert stub is not None
