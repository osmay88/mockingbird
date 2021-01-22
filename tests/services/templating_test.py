from mockingbird.services.templating_manager import render_template


def test_render_template(mocker):
    template = """
    {
        "username": "{{ username }}"
    }
    """

    expected = """
    {
        "username": "yocruxho"
    }
    """

    result = render_template(template, username="yocruxho")
    assert result == expected