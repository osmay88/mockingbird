from mockingbird.repository import IRepository


class SqlLittleRepository(IRepository):

    def __init__(self):
        # TODO: init the local database here
        pass

    def store_stub(self, item: dict):
        pass

    def clean_stub(self, stub_id: str = None, namespace: str = None):
        pass

    def get_url_hash(self, hash_url: str = None, stub_id: str = None):
        pass

    def store_url_hash(self, item: dict):
        pass

    def get_stubs(self, stub_id=None, namespace=None):
        pass