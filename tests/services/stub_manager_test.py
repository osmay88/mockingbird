from pytest_mock import MockerFixture
from mockingbird.services.stub_manager import create_stub, get_stub


def get_stubs_mocks(*args, **kwargs):
    stub_id = kwargs.get("stub_id")
    return [{
        "id": "this is an id",
        "namespace": "this_is_a_namespace",
        "stub": {
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
    }]


def init_mocks(mocker: MockerFixture):
    """
    init the most common mocks
    """
    def store_stub_mock(*args, **kwargs):
        return {
            "ResponseMetadata": {
                "HTTPStatusCode": 200
            }
        }
    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository._put_item_in_table",
        store_stub_mock
    )
    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository.get_url_hash",
        return_value=[]
    )
    mocker.patch(
        "mockingbird.repository.dynamo_repository.DynamoRepository.get_stubs",
        get_stubs_mocks
    )


def test_create_create_stub(mocker: MockerFixture):
    init_mocks(mocker)
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

    assert response["id"] is not None, "The new stub should have an id"
    assert response["namespace"] == "namespace", "the first part of the url should used as namespace"
    assert response["stub"] == stub_body


def test_create_stub_wrong_schema(mocker: MockerFixture):
    init_mocks(mocker)
    stub_body = {
        "response": {
            "status": 200,
            "body": "Hello world!",
            "headers": {
                "Content-Type": "text/plain"
            }
        }
    }
    try:
        create_stub(stub_body)
    except Exception as err:
        assert str(err) == "The schema validation for the stub failed with error: 'request' is a required property"
        return
    assert False, "An exception should have been thrown since the schema is invalid"


def test_get_all_stubs(mocker: MockerFixture):
    init_mocks(mocker)
    stubs = get_stub("any_random_id")
    assert len(stubs), "should contain a items array"
    assert len(stubs["items"]), "one item should be present"
