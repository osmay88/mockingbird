from pytest_mock import MockerFixture

from mockingbird.matchers import UrlMatcher

DEFAULT_HEADERS = {
    "Content-Type": "text/plain"
}

def create_stub(url, headers=DEFAULT_HEADERS, method="GET"):
    return {
        "request": {
            "method": method,
            "url": url,
            "headers": headers
        },
        "response": {
            "status": 200,
            "body": "Hello world!",
            "headers": {
                "Content-Type": "text/plain"
            }
        }
    }


def test_url_equal_to(mocker: MockerFixture):
    url = "/super/random/url?hello=33&rick=morty"
    stub = create_stub(url)
    assert UrlMatcher.url_equal_to(stub, url) is True


def test_url_not_equal_to(mocker: MockerFixture):
    url = "/super/random/url?hello=33&rick=morty"
    stub = create_stub(url)
    assert UrlMatcher.url_equal_to(stub, "%s&peter=griffin" % url) is False


def test_url_path_equal_to(mocker: MockerFixture):
    url = "/super/random/url?hello=33&rick=morty"
    stub = create_stub(url)
    assert UrlMatcher.url_path_equal_to(stub, "/super/random/url?hello=33&rick=morty")


def test_url_path_not_equal(mocker: MockerFixture):
    url = "/super/random/url?hello=33&rick=morty"
    stub = create_stub(url)
    assert not UrlMatcher.url_path_equal_to(stub, "/super/random/url2?hello=33&rick=morty")


def test_url_matching(mocker: MockerFixture):
    url = "/super/random/\\d+/url"
    stub = create_stub(url)
    assert UrlMatcher.url_matching(stub, "/super/random/123/url")
