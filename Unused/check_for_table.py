import boto3

dynamodb_client = boto3.client('dynamodb')

try:
    response = dynamodb_client.describe_table(TableName='test')
except dynamodb_client.exceptions.ResourceNotFoundException:
    # do something here as you require
    pass
