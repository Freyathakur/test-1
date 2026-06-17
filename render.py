from jinja2 import Template


def render(name: str) -> str:
    return Template("Hello {{ name }}").render(name=name)
