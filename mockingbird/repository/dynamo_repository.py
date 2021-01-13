import boto3
from boto3.dynamodb.conditions import Key

from mockingbird.utils.consts import URL_HASH_TABLE, STUBS_TABLE
from mockingbird.utils.logger import get_logger


log = get_logger("create_stub")


class DynamoRepository:
    def __init__(self, dynamo_url: str):
        self._client = boto3.resource("dynamodb", endpoint_url=dynamo_url)

    def _put_item_in_table(self, table_name, item):
        table = self._client.Table(table_name)
        response = table.put_item(Item=item)
        return response

    def get_stubs(self, stub_id=None, namespace=None):
        log.info("Getting stub with id %s" % stub_id)
        table = self._client.Table(STUBS_TABLE)
        if not id and not namespace:
            return table.scan().get("Items", [])
        response = table.query(KeyConditionExpression=Key('id').eq(stub_id))
        return response.get("Items")[0]

    def store_stub(self, item: dict):
        return self._put_item_in_table(STUBS_TABLE, item)

    def clean_stub(self, filter_query=None):
        pass

    def get_url_hash(self, hash_url: str):
        table = self._client.Table(URL_HASH_TABLE)
        result = table.query(KeyConditionExpression=Key('url_hash').eq(hash_url))
        return result.get("Items", [])

    def store_url_hash(self, item: dict):
        return self._put_item_in_table(URL_HASH_TABLE, item)
