import re
from mockingbird.utils import extract_path_url


class UrlMatcher:
    @staticmethod
    def url_equal_to(stub, url):
        """
        Check a url matches a stub url. Full comparison, including query params
        :return: True if  the url match the stub request url
        """
        stub_url = stub["request"]["url"]
        return stub_url == url

    @staticmethod
    def url_matching(stub, url: str):
        """
        Check if a url match a regular expression
        :param stub:
        :param url:
        :return:
        """
        stub_url = stub["request"]["url"]
        exp = re.compile(stub_url)
        return exp.fullmatch(url) is not None

    @staticmethod
    def url_path_equal_to(stub, url):
        """
        Validates two url but checking only the path, not query params
        :param stub:
        :param url:
        :return:
        """

        stub_url = stub["request"]["url"]
        stub_path = extract_path_url(stub_url)
        url_path = extract_path_url(url)
        return stub_path == url_path

    @staticmethod
    def url_path_matching(stub, pattern):
        """
        Check if the path regex match the url
        :param stub:
        :param pattern:
        :return:
        """
        stub_url = stub["request"]["url"]
        stub_path = extract_path_url(stub_url)
        exp = re.compile(pattern)
        return exp.fullmatch(stub_path) is not None
