"""
Here we implement all the utilities for aws
"""
import json


def make_response(code: int, body=None, error=None):
    response = {
        "statusCode": code,
        "body": body,
    }

    if error:
        response["body"] = json.dumps({
            "error": error
        })
    return response
