from pytest_mock import MockerFixture

from mockingbird.matchers import UrlMatcher


def create_stub(url):
    return {
        "request": {
            "method": "GET",
            "url": url
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
