import os
import boto3

from mockingbird.dynamo_tables import DYNAMO_TABLES

DYNAMODB = os.environ.get("DYNAMO_URL", "http://localhost:8000")


def create_secondary_index(secondary_index: dict):
    print("updating indexes for table %s" % secondary_index["TableName"])
    dynamodb = boto3.client('dynamodb', endpoint_url=DYNAMODB)
    dynamodb.update_table(**secondary_index)
    return


def create_table(table_def: dict, secondary_index: dict):
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMODB)
    print("Creating table %s" % table_def["TableName"])
    table = dynamodb.create_table(**table_def)
    if secondary_index:
        create_secondary_index(secondary_index)
    return table


for tbl, secondary_index in DYNAMO_TABLES:
    create_table(tbl, secondary_index)
