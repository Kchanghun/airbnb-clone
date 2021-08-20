from django import template

register = template.Library()


@register.filter
def sexycapitals(value):
    return value.capitalize()
