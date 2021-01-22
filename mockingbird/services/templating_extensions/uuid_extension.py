from jinja2 import nodes
from jinja2.ext import Extension


class UUIDExtension(Extension):
    tags = {"uuid"}

    def __init__(self, environment):
        super(UUIDExtension, self).__init__(environment)
        environment.extend(
            markdown_dir="uuid"
        )

    def parse(self, parser):
        line_no = next(parser.stream).lineno

        return nodes.CallBlock(
            self.call_method("_get_uuid"), [], [], ''
        ).set_lineno(line_no)

    def _get_uuid(self, *args, **kwargs):
        import uuid
        uuid_ = uuid.uuid4()
        return uuid_.hex
