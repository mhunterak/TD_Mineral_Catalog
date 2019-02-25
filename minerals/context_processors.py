'''
Context Processors do some pretty great work, like default arguments supplied
to templates when they're rendered. kind of like Macros in Flask, but even more
powerful.
'''
import string

from django.utils.datastructures import MultiValueDictKeyError

from .forms import SearchForm
from .static_vars import COLORS, GROUPS


def search_form(request):
    '''renders the search form still uses a <form> wrapper to control action
    Now pulls the query from the request data and presents it as the
    initial field value
    '''
    try:
        query = request.POST['search']
    except MultiValueDictKeyError:
        query = ""
    return {
        'SearchForm': SearchForm(initial={'search': query}),
    }


def alphabet(request):
    '''renders the capitol alphabet from A-Z'''
    return {
        'alphabet': string.ascii_uppercase,
    }


def groups(request):
    '''renders the mineral groups'''
    return {'groups': GROUPS, }


def colors(request):
    '''renders the available colors'''
    return {'colors': COLORS, }
