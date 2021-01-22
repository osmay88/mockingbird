from pytest_mock import MockerFixture

from mockingbird.main import mock_it


def test_mock_it(mocker: MockerFixture):
    result = mock_it(dict(), None)
    assert True
