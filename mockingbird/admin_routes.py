import json
from mockingbird.services import stub_manager
from mockingbird.utils.logger import get_logger
from mockingbird.utils.decimal_encoder import DecimalEncoder


def create_stub(event: dict, context):
    """
    Stores a new stub in the database.
    """
    log = get_logger("create_stub_route")

    body = event.get("body")
    if not body:
        return {
            "statusCode": 400,
            "body": "Request body is missing"
        }

    data = json.loads(body)
    log.info("stub to create %s" % json.dumps(data))
    try:
        response = stub_manager.create_stub(data)
        log.info("Created stub %s" % response)
        return {
            'statusCode': 200,
            'body': json.dumps(response, cls=DecimalEncoder)
        }
    except Exception as err:
        print(err)

        return {
            'statusCode': 500,
            'body': json.dumps(str(err))
        }


def get_all_stubs(event, context):
    """
    returns all the stubs in the db
    """
    stubs = stub_manager.get_all_stubs()
    return {
        "statusCode": 200,
        "body": json.dumps(stubs, cls=DecimalEncoder)
    }
