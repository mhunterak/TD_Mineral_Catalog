from django import template

register = template.Library()

@register.filter
def under_space(value):
    '''
This template filter replaces an underscore with a space:
'crystal_symmetry' becomes 'crystal symmetry'
    '''
    return value.replace("_", " ")+":"
