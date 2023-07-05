import datetime
import json

def hello(event, context):
    body = {
        "message": "Serverless CI/CD Demo",
        "version": "v1.0",
        "timestamp": datetime.utcnow()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
