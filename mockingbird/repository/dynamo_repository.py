import boto3
from boto3.dynamodb.conditions import Key

# from mockingbird.utils.consts import URL_HASH_TABLE, STUBS_TABLE
from mockingbird.dynamo_tables import (STUB_TBL,
                                       STUB_TABLE_NAME,
                                       PATTERN_HASH_TBL,
                                       PATTERN_HASH_TABLE_NAME, PATTERN_HASH_TBL_NAMESPACE_INDEX, )
from mockingbird.dynamo_tables.stub_tbl import STUB_TBL_NAMESPACE_INDEX
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

    def _delete_item_from_table(self, table_name, object_id, namespace=None):
        table = self._client.Table(table_name)
        query = {
            "stub_id": object_id,
        }
        if namespace:
            query["namespace"] = namespace
        return table.delete_item(Key=query)

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
        response = None

        # no filter defined, we return the whole table
        # TODO: think about disabling this for performance
        if not stub_id and not namespace:
            response = table.scan()

        if stub_id:  # TODO refactor the shit out of this
            query = Key('id').eq(stub_id)
            log.info("Using id as key for query")
            response = table.query(KeyConditionExpression=query)
        if namespace and stub_id:
            query = Key('id').eq(stub_id) & Key("namespace").eq(namespace)
            log.info("Using id and namespace as key for query")
            response = table.query(KeyConditionExpression=query)
        elif not stub_id and namespace:
            log.info("Using namespace as key for query")
            query = Key("namespace").eq(namespace)
            response = table.query(IndexName=STUB_TBL_NAMESPACE_INDEX, KeyConditionExpression=query)

        if response and response.get("Items"):
            return response.get("Items", [])
        return []

    def store_stub(self, item: dict):
        return self._put_item_in_table(STUB_TABLE_NAME, item)

    def clean_stub(self, stub_id: str = None, namespace: str = None):
        response = self._delete_item_from_table(STUB_TABLE_NAME, stub_id, namespace=namespace)
        if response:  # if the stub was deleted also clean the hash table
            self._delete_item_from_table(PATTERN_HASH_TABLE_NAME, stub_id)

    def get_url_hash(self, hash_url: str = None, stub_id: str = None):
        table = self._client.Table(PATTERN_HASH_TABLE_NAME)
        result = None
        if not hash_url and not stub_id:
            result = table.scan()  # return all the items in the table

        if hash_url and not stub_id:  # TODO: refactor this shit
            result = table.query(KeyConditionExpression=Key('url_hash').eq(hash_url))
        elif not hash_url and stub_id:  # filter by secondary index
            result = table.query(IndexName=PATTERN_HASH_TBL_NAMESPACE_INDEX, KeyConditionExpression=Key("stub_id").eq(stub_id))
        else:
            result = table.query(KeyConditionExpression=Key('url_hash').eq(hash_url) & Key("stub_id").eq(stub_id))
        return result.get("Items", [])

    def store_url_hash(self, item: dict):
        return self._put_item_in_table(PATTERN_HASH_TABLE_NAME, item)
