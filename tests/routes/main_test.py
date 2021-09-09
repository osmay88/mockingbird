import pytest
from pytest_mock import MockerFixture

from mockingbird.routes.mock_it import mock_it


@pytest.mark.skip("enable later when the route is done")
def test_mock_it(mocker: MockerFixture):
    result = mock_it(dict(), None)
    assert True
