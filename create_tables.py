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

PATTERN_HASH = {
    "TableName": "Mockingbird_Pattern_Hash",
    "KeySchema": [
        {"AttributeName": "url_hash", "KeyType": "HASH"},
        {"AttributeName": "stub_id", "KeyType": "RANGE"},
    ],
    "AttributeDefinitions": [
        {"AttributeName": "url_hash", "AttributeType": "S"},
        {"AttributeName": "stub_id", "AttributeType": "S"},
    ],
    "BillingMode": "PAY_PER_REQUEST"
}


def create_table(table_def: dict):
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMODB)
    table = dynamodb.create_table(**table_def)
    return table


create_table(STUB_TBL)
create_table(PATTERN_HASH)
