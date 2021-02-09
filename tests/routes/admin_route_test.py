import json
from os import environ
from pytest_mock import MockerFixture
from mockingbird.routes.admin_routes import create_stub


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


def test_create_stub_empty_body(mocker: MockerFixture):
    new_stub_request = {
        "body": ""
    }
    response = create_stub(new_stub_request, None)
    assert response['statusCode'] == 400
    assert json.loads(response.get("body")) == {"error": "Missing request body"}


def test_create_stub_already_exists(mocker: MockerFixture):
    environ["MOCKINGBIRD_STORAGE"] = "Dynamo"

    def get_url_hash_mock(*args, **kwargs):
        return [{
            "stub_id": "this_is_an_existing_stub"
        }]

    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository.get_url_hash",
        get_url_hash_mock
    )

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

    response = create_stub(new_stub_request, None)
    assert response['statusCode'] == 400
    assert json.loads(response.get("body")) == {"error": "An stub already exist using the same url pattern, stub id: this_is_an_existing_stub"}
