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

STUB_TBL_SECONDARY_INDEX = {
    "TableName": TABLE_NAME,
    "AttributeDefinitions": [
        {
            "AttributeName": "namespace",
            "AttributeType": "S"
        },
    ],
    "GlobalSecondaryIndexUpdates": [
        {
            "Create": {
                "IndexName": "NamespaceIndex",
                "KeySchema": [
                    {
                        "AttributeName": "namespace",
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
