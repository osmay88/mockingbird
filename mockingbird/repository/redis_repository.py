import redis

from mockingbird.repository import IRepository


class RedisRepository(IRepository):
    def store_stub(self, item: dict):
        pass

    def clean_stub(self, filter_query=None):
        pass

    def get_url_hash(self, hash_url: str):
        pass

    def store_url_hash(self, item: dict):
        pass

    def get_stubs(self, stub_id=None, namespace=None):
        pass

    def __init__(self, host, port, password=None):
        self._client = redis.Redis(host, port, password)
