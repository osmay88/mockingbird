import abc


class IRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_stubs(self, stub_id=None, namespace=None):
        raise NotImplemented("Method not implemented")

    @abc.abstractmethod
    def store_stub(self, item: dict):
        raise NotImplemented("Method not implemented")

    @abc.abstractmethod
    def clean_stub(self, filter_query=None):
        raise NotImplemented("Method not implemented")

    @abc.abstractmethod
    def get_url_hash(self, hash_url: str):
        raise NotImplemented("Method not implemented")

    @abc.abstractmethod
    def store_url_hash(self, item: dict):
        raise NotImplemented("Method not implemented")
