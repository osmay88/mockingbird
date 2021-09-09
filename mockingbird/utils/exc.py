import json


class MockingException(Exception):
    def __init__(self, msg, error_code, http_status_code=None, *args, **kwargs):
        super(MockingException, self).__init__(*args, **kwargs)
        self.msg = msg
        self.error_code = error_code
        self.http_status_code = http_status_code

    def to_json(self):
        return {
            "error_code": self.error_code,
            "error": self.msg,
        }

    def __repr__(self):
        return json.dumps(self.to_json())

    def __str__(self):
        return json.dumps(self.to_json())
