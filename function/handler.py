import urllib3

import json

def handler(event, context):

    # Creating a PoolManager instance for sending requests.
    http = urllib3.PoolManager()

    # not parameterized yet, will worry about that later
    request_endpoint = 'http://arkhamdb.com/api/public/card/01001'
    response = http.request("GET", request_endpoint)

 
    return {
        'statusCode': 200,
        'body': response.data
    }