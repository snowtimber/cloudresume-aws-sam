import json
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    #1. Parse out query string params
    visitorip = event['queryStringParameters']['ip']
    visitordatetime = event['queryStringParameters']['datetime']

    print('visitorip=' + visitorip)
    print('visitordatetime=' + visitordatetime)

    #2. Construct the body of the response object
    #transactionResponse = {}
    #transactionResponse['transactionid'] = transactionId
    #transactionResponse['type'] = transactionType
    #transactionResponse['message'] = 'Hello from Lambda land'

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table("visitors")
    print(table.table_status)

    dbresponse = table.update_item(
        Key={
            'ip': visitorip
            #'title': title
        },
        UpdateExpression="set info.datetime=:a",
        #UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            #':r': Decimal(rating),
            #':p': plot,
            ':a': visitordatetime
            #':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    #return dbresponse
    print('dbresponse=' + ReturnValues)

    #query table
    scanresponse = table.scan()
    data = scanresponse['Items']

    #Scan has 1 MB limit on the amount of data it will return in a request, so we need to paginate through the results in a loop.
    while 'LastEvaluatedKey' in scanresponse:
        scanresponse = table.scan(ExclusiveStartKey=scanresponse['LastEvaluatedKey'])
        data.extend(scanresponse['Items'])
        uniqueip = 0

    #count through all items
    for item in data:
        print(item['ip'], ":", item['datetime'])
        uniqueip += 1

    #return scanresponse
    print('scanresponse=' + scanresponse)
    #return data
    print('data=' + data)
    print('count uniqueip=' + uniqueip)

    #2. Construct the body of the response object
    #transactionResponse = {}
    #transactionResponse['transactionid'] = transactionId
    #transactionResponse['type'] = transactionType
    #transactionResponse['message'] = 'Hello from Lambda land'


    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['headers']['Access-Control-Allow-Origin'] = 'https://heyitslogan.com'
    responseObject['body'] = json.dumps(uniqueip)

    #4. Return the response object
    return responseObject #the end
