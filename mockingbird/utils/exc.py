import json


class MockingException(BaseException):
    def __init__(self, msg, code, *args, **kwargs):
        super(MockingException, self).__init__(*args, **kwargs)
        self.msg = msg
        self.code = code

    def to_json(self):
        return {
            "code": self.code,
            "error": self.code,
        }

    def __repr__(self):
        return json.dumps(self.to_json())

    def __str__(self):
        return json.dumps(self.to_json())
