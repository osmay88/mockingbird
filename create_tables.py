import os
import boto3


DYNAMODB = os.environ.get("DYNAMO_URL", "http://localhost:8000")

STUB_TBL = {
    "TableName": "Mockingbird_Stubs",
    "KeySchema": [
        {"AttributeName": "id", "KeyType": "HASH"},
        {"AttributeName": "namespace", "KeyType": "RANGE"},
    ],
    "AttributeDefinitions": [
        {"AttributeName": "id", "AttributeType": "S"},
        {"AttributeName": "namespace", "AttributeType": "S"},
    ],
    "BillingMode": "PAY_PER_REQUEST"
}


def create_table(table_def: dict):
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMODB)
    table = dynamodb.create_table(**table_def)
    return table


create_table(STUB_TBL)
