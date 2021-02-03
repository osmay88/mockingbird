import boto3
from boto3.dynamodb.conditions import Key

# from mockingbird.utils.consts import URL_HASH_TABLE, STUBS_TABLE
from mockingbird.dynamo_tables import (STUB_TBL,
                                       STUB_TABLE_NAME,
                                       PATTERN_HASH_TBL,
                                       PATTERN_HASH_TABLE_NAME,)
from mockingbird.repository import IRepository
from mockingbird.utils.logger import get_logger


log = get_logger("create_stub")


class DynamoRepository(IRepository):
    def __init__(self, dynamo_url: str):
        self._client = boto3.resource("dynamodb", endpoint_url=dynamo_url)

    def _put_item_in_table(self, table_name, item):
        table = self._client.Table(table_name)
        response = table.put_item(Item=item)
        return response

    def get_stubs(self, stub_id=None, namespace=None):
        """
        Returns a list of stubs from the db. If not id or namespace
        is provided then return a list of all the stubs in the database

        :param stub_id: Filter using the stub id field
        :param namespace: Filter using the stub namespace
        :return: List of stubs
        """
        log.info("Getting stub with id %s and namespace %s" % (stub_id, namespace))
        table = self._client.Table(STUB_TABLE_NAME)

        # no filter defined, we return the whole table
        # TODO: think about disabling this for performance
        if not stub_id and not namespace:
            return table.scan().get("Items", [])

        if stub_id:  # TODO refactor the shit out of this
            query = Key('id').eq(stub_id)
            index_name = None
            log.info("using id as key for query")
        if namespace and stub_id:
            query = Key('id').eq(stub_id) & Key("namespace").eq(namespace)
            index_name = None
            log.info("using id and namespace as key for query")
        elif not stub_id and namespace:
            log.info("using namespace as key for query")
            index_name = "NamespaceIndex"
            query = Key("namespace").eq(namespace)
        if index_name:
            response = table.query(IndexName="NamespaceIndex", KeyConditionExpression=query)
        else:
            response = table.query(KeyConditionExpression=query)
        if response.get("Items"):
            return response.get("Items")
        return []

    def store_stub(self, item: dict):
        return self._put_item_in_table(STUB_TABLE_NAME, item)

    def clean_stub(self, filter_query=None):
        pass

    def get_url_hash(self, hash_url: str):
        table = self._client.Table(PATTERN_HASH_TABLE_NAME)
        result = table.query(KeyConditionExpression=Key('url_hash').eq(hash_url))
        return result.get("Items", [])

    def store_url_hash(self, item: dict):
        return self._put_item_in_table(PATTERN_HASH_TABLE_NAME, item)
