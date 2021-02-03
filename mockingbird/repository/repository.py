"""
General implementation of the repository class
"""
import os

from mockingbird.repository import IRepository
from mockingbird.repository.dynamo_repository import DynamoRepository

STORAGE_OPTIONS = [
    "Redis",
    "Dynamo"
]


class Repository:
    def __init__(self):
        pass

    @staticmethod
    def get_repository() -> IRepository:
        """
        return an instance of the IRepository class
        """
        storage_cls = os.environ.get("MOCKINGBIRD_STORAGE", "Dynamo")
        if storage_cls == "Dynamo":
            dynamo_db = os.environ.get("DYNAMO_URL")
            return DynamoRepository(dynamo_url=dynamo_db)
        elif storage_cls == "Redis":
            raise NotImplemented("Redis storage not impleted yet")
        else:
            raise Exception("Unknown storage system, valid options are: %s" % STORAGE_OPTIONS)
