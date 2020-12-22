import boto3
from boto3.dynamodb.conditions import Key


class DynamoRepository:
    def __init__(self, dynamo_url: str):
        self._client = boto3.resource("dynamodb", endpoint_url=dynamo_url)

    def get_stubs(self, table_name, id=None):
        table = self._client.Table(table_name)
        if not id:
            return table.scan().get("Items", [])
        response = table.query(KeyConditionExpression=Key('Id').eq(id))
        return response.get("Items")[0]

    def store_stub(self, table_name:str, item: dict):
        table = self._client.Table(table_name)
        response = table.put_item(Item=item)
        return response

    def clean_stub(self, filter=None):
        pass

