import boto3
import json
import logging
from os import getenv
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)


def parse_records(event):
    """Take in the list of events from SQS and return only the data we want to store"""
    parsed = []
    for record in event.get('Records', []):
        try:
            body = json.loads(record['body'])
            parsed.append(dict(AccountId=body['AccountId'], SecretAccessKey=body['SecretKey'], AccessKey=body['AccessKey']))
        except Exception as e:
            logger.error(f"Could not parse SNS event due to: {e}")
            body = record['body']
            parsed.append(dict(AccountId=body['AccountId'], SecretAccessKey=body['SecretKey'], AccessKey=body['AccessKey']))
    return parsed


def exists(parsed_entry, table):
    response = table.query(
        KeyConditionExpression=Key('accountId').eq(parsed_entry['AccountId'])
    )
    if len(response['Items']) > 0:
        return True
    else:
        return False

def flush_to_database(parsed_entry, table):
    """Write out record to dynamodb"""
    if exists(parsed_entry, table):
        table.delete_item(
            Key={
                'accountId': parsed_entry['AccountId']
            }
        )

    table.put_item(
        Item={
            'accountId': parsed_entry['AccountId'],
            'AccessKey': parsed_entry['AccessKey'],
            'SecretAccessKey': parsed_entry['SecretAccessKey']
        }
    )

def lambda_handler(event, context):
    parsed = parse_records(event)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(getenv('MY_DYNAMODB_TABLE'))

    for entry in parsed:
        flush_to_database(entry, table)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "SQS Run complete."
        }),
    }
