import json
from datetime import datetime
import ssl
import socket
import re

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
        if "queryStringParameters" in event and event["queryStringParameters"] and "url" in event["queryStringParameters"]:
            url = event["queryStringParameters"]["url"]
        else:
            return unsupported
    else:
        return unsupported

    return {
        "statusCode": 200,
        "body": json.dumps(check_ssl_data(url), indent=4)
    }


# Takes a URL as input and returns a formatted json object
def check_ssl_data(url):
    # removing the http or https at the beginning. Pretty sure http wouldnt work for this though
    if re.search(r"^http[s]?:\/\/", url):
        url = re.split(r"^http[s]?:\/\/", url)[1]    
    context = ssl.create_default_context()
    context.check_hostname = False
    conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=url)
    conn.settimeout(2.0)
    ssl_info = None
    try:
        conn.connect((url, 443))
        ssl_info = conn.getpeercert()
    except socket.gaierror as e:
        return {
            "statusCode": 400,
            "body": "Invalid URL: %s" % url
        }
    expired = False
    if datetime.strptime(ssl_info["notAfter"], r'%b %d %H:%M:%S %Y %Z') <= datetime.today():
        expired = True
    return {
        "hostname": url,
        "validFrom": str(datetime.strptime(ssl_info["notBefore"], r'%b %d %H:%M:%S %Y %Z')),
        "validTo": str(datetime.strptime(ssl_info["notAfter"], r'%b %d %H:%M:%S %Y %Z')),
        "expired": expired
    }
