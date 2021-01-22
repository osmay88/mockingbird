TABLE_NAME = "Mockingbird_Stubs"

STUB_TBL = {
    "TableName": TABLE_NAME,
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