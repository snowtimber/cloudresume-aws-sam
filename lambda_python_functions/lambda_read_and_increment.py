#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
import json
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_data_handler(ip, date_time, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('dynamodb_resume_visitors_table')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("Get movie succeeded:")
        pprint(movie, sort_dicts=False)

#another sample python script

def get_data_handler(event, context):
    '''When this function is invoked - retrive visitor count, add one, store
    in database, return to client '''
    dynamodb = boto3.client('dynamodb')

    # Get Visits
    response = dynamodb.get_item(
        TableName='dynamodb_resume_visitors_table',
        Key={'VisitorID': {'S': '0'}}
        )

    visits = int(response["Item"]["Visits"]["N"]) + 1

    # Store Visits
    dynamodb.put_item(TableName='dynamodb_resume_visitors_table', Item={
        'Site': {'N': '0'},
        'Visits': {'N': str(visits)}
    })
    return visits
