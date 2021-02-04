from os import environ
from pytest_mock import MockerFixture

from mockingbird.repository import IRepository
from mockingbird.repository.dynamo_repository import DynamoRepository
from mockingbird.repository.redis_repository import RedisRepository
from mockingbird.repository.repository import Repository, REDIS_OPTION


def test_repository_builder(mocker: MockerFixture):
    repository = Repository.get_repository()
    assert isinstance(repository, IRepository), "Repository class doesn't implement IRepository interface"
    assert isinstance(repository, DynamoRepository), "Should default to Dynamodb repository class"


def test_build_redis_repository(mocker: MockerFixture):
    environ["MOCKINGBIRD_STORAGE"] = REDIS_OPTION
    repository = Repository.get_repository()
    assert isinstance(repository, IRepository), "Repository class doesn't implement IRepository interface"
    assert isinstance(repository, RedisRepository), "Should default to Dynamodb repository class"
