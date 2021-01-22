TABLE_NAME = "Mockingbird_Pattern_Hash"

PATTERN_HASH_TBL = {
    "TableName": TABLE_NAME,
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
