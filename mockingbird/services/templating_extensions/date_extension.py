from jinja2 import nodes
from jinja2.ext import Extension


class DateExtension(Extension):
    tags = {"date"}

    def __init__(self, environment):
        super(DateExtension, self).__init__(environment)
        environment.extend(
            markdown_dir="date"
        )

    def parse(self, parser):
        line_no = next(parser.stream).lineno
        args = [parser.parse_expression()]

        return nodes.CallBlock(
            self.call_method("_get_date", args), [], [], ''
        ).set_lineno(line_no)

    def _get_date(self, format_str="iso", **kwargs):
        from datetime import datetime
        now = datetime.now()
        if format_str:
            return now.strftime(format_str)
        return datetime.utcnow().isoformat()
