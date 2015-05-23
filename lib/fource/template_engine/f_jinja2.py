from jinja2 import Template
import json


class Jinja2Engine(object):
    """
    Jinja2 template engine class
    """

    def render_from_object(self, object, **data):
        template_str = json.dumps(object)
        result = self.render(template_str, **data)
        return json.loads(result)

    def render(self, template_str, **data):
        template = Template(template_str)
        return template.render(**data)
