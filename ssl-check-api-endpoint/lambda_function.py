import json

def lambda_handler(event, context):
    # POC function that will return the url that was passed to the api and the request itself for testing
    return {
        'statusCode': 200,
        'body': {
            "your_url": event['url'],
            "event": event    
        },
    }
