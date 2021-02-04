"""
General implementation of the repository class
"""
import os

from mockingbird.repository import IRepository
from mockingbird.repository.dynamo_repository import DynamoRepository
from mockingbird.repository.redis_repository import RedisRepository

REDIS_OPTION = "Redis"
DYNAMO_OPTION = "Dynamo"

STORAGE_OPTIONS = [
    REDIS_OPTION,
    DYNAMO_OPTION
]


class Repository:
    def __init__(self):
        pass

    @staticmethod
    def get_repository() -> IRepository:
        """
        return an instance of the IRepository class
        """
        storage_cls = os.environ.get("MOCKINGBIRD_STORAGE", DYNAMO_OPTION)
        if storage_cls == DYNAMO_OPTION:
            dynamo_db = os.environ.get("MOCKINGBIRD_DYNAMO_URL")
            return DynamoRepository(dynamo_url=dynamo_db)
        elif storage_cls == REDIS_OPTION:
            redis_host = os.environ.get("MOCKINGBIRD_REDIS_HOST")
            redis_port = os.environ.get("MOCKINGBIRD_REDIS_PORT")
            redis_password = os.environ.get("MOCKINGBIRD_REDIS_PASSWORD")
            return RedisRepository(host=redis_host, port=redis_port, password=redis_password)
        else:
            raise Exception("Unknown storage system, valid options are: %s" % STORAGE_OPTIONS)
