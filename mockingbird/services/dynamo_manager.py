import boto3
import uuid


class DynamoClient:
    def __init__(self, table: str, dynamo_url: str):
        self._client = boto3.resource("dynamodb", endpoint_url=dynamo_url)

    def store_item(self, table_name: str, item: dict):
        table = self._client.Table(table_name)
        response = table.put_item(item)
        return response


    def get_items(self, *args, **kwargs):
        pass

