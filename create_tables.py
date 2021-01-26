import os
import boto3

from mockingbird.dynamo_tables import DYNAMO_TABLES

DYNAMODB = os.environ.get("DYNAMO_URL", "http://localhost:8000")


def create_table(table_def: dict):
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMODB)
    table = dynamodb.create_table(**table_def)
    return table


for tbl in DYNAMO_TABLES:
    create_table(tbl)
