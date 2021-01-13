"""
Here we implement all the utilities for aws
"""


def make_response(code: int, message: str):
    return {
        "statusCode": code,
        "body": message,
    }
