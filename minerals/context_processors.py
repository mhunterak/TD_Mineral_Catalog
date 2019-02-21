'''
Context Processors do some pretty great work, like default arguments supplied
to templates when they're rendered.
'''

import string
import re

from .forms import SearchForm
from .models import Mineral

from .static_vars import COLORS, GROUPS


def search_form(request):
    '''
renders the search form - still needs a <form> wrapper to control action
    '''
    return {
        'SearchForm': SearchForm()
    }


def alphabet(request):
    '''
renders the capitol alphabet from A-Z
    '''
    return {
        'alphabet': string.ascii_uppercase,
    }


def groups(request):
    '''
renders the mineral groups
    '''
    return {'groups': GROUPS, }


def colors(request):
    '''
renders the colors available
    '''
    return {'colors': COLORS, }
