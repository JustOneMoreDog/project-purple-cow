import json

def lambda_handler(event, context):
    # POC function that will return the url that was passed to the api and the request itself for testing
    # This time the POC works
    unsupported = {
        'statusCode': 404,
        'body': "Unsupported"
    }
    # Making sure that the right api endpoint is called with the right method
    if event["path"] == "/ssl-check" and event["httpMethod"] == "GET":
        # Making sure that params were passed correctly
        if "queryStringParameters" in event and "url" in event["queryStringParameters"]:
            url = event["queryStringParameters"]["url"]
        else:
            return unsupported
    else:
        return unsupported
    return {
        'statusCode': 200,
        'body': "URL passed was %s" % url,
    }
