TABLE_NAME = "Mockingbird_Call_Log"

CALL_LOG_TABLE = {
    "TableName": TABLE_NAME,
    "KeySchema": [
        {"AttributeName": "stub_id", "KeyType": "HASH"},
        {"AttributeName": "namespace", "KeyType": "RANGE"},
    ],
    "AttributeDefinitions": [
        {"AttributeName": "stub_id", "AttributeType": "S"},
        {"AttributeName": "namespace", "AttributeType": "S"},
    ],
    "BillingMode": "PAY_PER_REQUEST"
}
