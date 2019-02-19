'''
Context Processors do some pretty great work, like default arguments supplied
to templates when they're rendered.
'''

import string
import re

from .forms import SearchForm
from .static_vars import GROUPS
from .models import Mineral


def search_form(request):
    return {
        'SearchForm': SearchForm()
    }


def alphabet(request):
    return {
        'alphabet': string.ascii_uppercase,
    }


def groups(request):
    GROUPS.sort()
    return {'groups': GROUPS, }


# this queryset is loaded once on initialization
all_minerals = Mineral.objects.all()


def colors(request):
    color_list = []
    for mineral in all_minerals:
        new_color = mineral.color.lower()
        if new_color not in color_list:
            if new_color != '':
                if not re.search('\W', new_color):
                    color_list.append(new_color)
    color_list.sort()
    return {'colors': color_list, }
