STUB_REQUEST = {
    "type": "object",
    "properties": {
        "method": { "type": "string", "enum": ["GET", "POST", "PUT", "PATCH", "DELETE"]},
        "url": { "type": "string" }
    }
}

STUB_RESPONSE = {
    "status": {
        "type": "integer"
    },
    "body": {
        "type": "string",
        "default": ""
    },
    "headers": {
        "type": "object",
        "additionalProperties": True
    }
}

STUB_OBJECT = {
    "type": "object",
    "properties": {
        "request": STUB_REQUEST,
        "response": STUB_RESPONSE
    }
}
