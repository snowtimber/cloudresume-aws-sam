#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.htmlhttps://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
#sample lambda python code to
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def write_ip_datetime_handler(ip, datetime, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('visitors')
    response = table.put_item(
       Item={
            'ip': ip,
            'datetime': datetime,
            }
        }
    )
    return response

def query_visitors(ip, datetime, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('visitors')
    print(f"Get count of unique ip, get separate count of unique ip & datetime")
    ##print(f"Get year, title, genres, and lead actor")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={"ip": "ip"},
        KeyConditionExpression=
            Key('year').eq(year) & Key('title').between(title_range[0], title_range[1])
    )
    return response['Items']




if __name__ == '__main__':
    visitor_resp = write_ip_datetime_handler("192.168.0.0", "12/12/0000 "
        + randint(0, 24)":"
        + randint(0, 60)":"
        + randint(0, 60)
        , 0)
    print("Put ip & datetime succeeded:")
    pprint(visitor_resp, sort_dicts=False)

if __name__ == '__main__':
    query_year = 1992
    query_range = ('A', 'L')
    print(f"Get movies from {query_year} with titles from "
          f"{query_range[0]} to {query_range[1]}")
    movies = query_visitors(query_year, query_range)
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}")
        pprint(movie['info'])
