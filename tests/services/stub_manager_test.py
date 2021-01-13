from pytest_mock import MockerFixture

from tests import *
from mockingbird.services.stub_manager import create_stub


def test_create_create_stub(mocker: MockerFixture):
    def store_stub_mock(*args, **kwargs):
        return {
            "ResponseMetadata": {
                "HTTPStatusCode": 200
            }
        }
    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository.store_stub",
        store_stub_mock
    )
    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository.store_url_hash",
        store_stub_mock
    )

    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository.get_url_hash",
        return_value=[]
    )

    stub_body = {
        "request": {
            "method": "GET",
            "url": "/namespace/thing"
        },
        "response": {
            "status": 200,
            "body": "Hello world!",
            "headers": {
                "Content-Type": "text/plain"
            }
        }
    }

    response = create_stub(stub_body)

    assert response["id"] is not None
    assert response["namespace"] == "namespace"
    assert response["stub"] == stub_body
