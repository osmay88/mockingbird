from  datetime import datetime
from pytest_mock import MockerFixture
from mockingbird.services.templating_manager import render_template


def test_render_template(mocker: MockerFixture):
    today = datetime.now().strftime("%Y-%m-%d")
    template = """ hello {{ username }} today is {% date '%Y-%m-%d' %} """
    result = render_template(template, username="osmay")
    assert result == """ hello osmay today is %s """ % today


def test_render_uuid(mocker: MockerFixture):
    template = "hello this is a uuid {% uuid %}"
    result = render_template(template)
    assert len(result) == 53
