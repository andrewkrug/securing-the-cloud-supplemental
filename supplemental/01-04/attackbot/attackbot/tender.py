"""Tend the curated set of accounts."""


import boto3
import os
import uuid


def lambda_handler(event, context={}):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.getenv("MY_DYNAMODB_TABLE"))

    response = table.scan()
    items = response.get("Items")
    last_evaluated = response.get("LastEvaluatedKey")
    while last_evaluated:
        response = table.scan(
            ExclusiveStartKey=last_evaluated
        )
        item.extend(response.get("Items"))
        last_evaluated = response.get("LastEvaluatedKey")

    for item in items:
        item['uuid'] = uuid.uuid4().hex
        table.put_item(Item=item)

    return True