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

PATTERN_HASH_TBL_NAMESPACE_INDEX = "StubIdIndex"

PATTERN_HASH_TBL_SECONDARY_INDEX = {
    "TableName": TABLE_NAME,
    "AttributeDefinitions": [
        {
            "AttributeName": "stub_id",
            "AttributeType": "S"
        },
    ],
    "GlobalSecondaryIndexUpdates": [
        {
            "Create": {
                "IndexName": PATTERN_HASH_TBL_NAMESPACE_INDEX,
                "KeySchema": [
                    {
                        "AttributeName": "stub_id",
                        "KeyType": "HASH"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                },
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1,
                }
            }
        }
    ],
}
