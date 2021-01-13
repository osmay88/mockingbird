import boto3
from boto3.dynamodb.conditions import Key
from mockingbird.utils.logger import get_logger


log = get_logger("create_stub")


class DynamoRepository:
    def __init__(self, dynamo_url: str):
        self._client = boto3.resource("dynamodb", endpoint_url=dynamo_url)

    def _put_item_in_table(self, table_name, item):
        table = self._client.Table(table_name)
        response = table.put_item(Item=item)
        return response

    def get_stubs(self, table_name, id=None, namespace=None):
        log.info("Getting stub with id %s" % id)
        table = self._client.Table(table_name)
        if not id and not namespace:
            return table.scan().get("Items", [])
        response = table.query(KeyConditionExpression=Key('id').eq(id))
        return response.get("Items")[0]

    def store_stub(self, table_name: str, item: dict):
        return self._put_item_in_table(table_name, item)

    def clean_stub(self, filter=None):
        pass

    def get_url_hash(self, table_name: str, hash: str):
        table = self._client.Table(table_name)
        result = table.query(KeyConditionExpression=Key('url_hash').eq(hash))
        return result.get("Items", [])

    def store_url_hash(self, table_name: str, item: dict):
        return self._put_item_in_table(table_name, item)
