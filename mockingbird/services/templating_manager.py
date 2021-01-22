from jinja2 import Environment

from mockingbird.services.templating_extensions import EXTENSIONS


def render_template(template_text, **kwargs):
    # template = jinja2.Template(template_text)
    template = Environment(extensions=EXTENSIONS).from_string(template_text)
    return template.render(**kwargs)
