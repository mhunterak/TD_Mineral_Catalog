from django import template

register = template.Library()

@register.filter
def under_space(value):
    return value.replace("_", " ")+":"
