from django import template


register = template.Library()
default_image = '/static/images/default.jpg'


@register.filter()
def mediapath(path):
    if path:
        return f"/media/{path}"
    return default_image


@register.simple_tag()
def mediapath_tag(path):
    if path:
        return f"/media/{path}"
    return default_image
