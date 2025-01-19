from django import template

register = template.Library()


@register.filter(name="media_filter")
def media_filter(value):
    if value:
        return value.url
    return "/static/catalog/images/default.png"
