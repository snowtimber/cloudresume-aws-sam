#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.htmlhttps://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
#sample lambda python code to
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def write_ip_datetime_handler(ip, datetime, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('visitors')
    putresponse = table.put_item(
       Item={
            'ip': ip,
            'datetime': datetime,
            }
    )

    return putresponse

    response = table.scan()
    data = response['Items']

    #Scan has 1 MB limit on the amount of data it will return in a request, so we need to paginate through the results in a loop.
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    for item in data:
        print(item['ip'], ":", item['datetime'])

    return response
    return data
