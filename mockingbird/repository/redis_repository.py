import redis


class RedisRepository:
    def __init__(self, host, port, password):
        self._client = redis.Redis(host, port, password)

    def store_stub(self, stub: dict):
        pass

    def delete_stub(self, stub_id):
        pass

    def store_request(self, request):
        pass

    def delete_request(self, request):
        pass

