'''
Context Processors do some pretty great work, like default arguments supplied
to templates when they're rendered.
'''

import string
import re

from .forms import SearchForm
from .models import Mineral


# this queryset is loaded once on initialization
all_minerals = Mineral.objects.all()
all_minerals.count()


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
    group_list = []
    groups = all_minerals.values('group').distinct()
    for group in groups:
        group_list.append(group['group'])
    group_list.sort()
    return {'groups': group_list, }


def colors(request):
    '''
renders the colors available
    '''
    color_list = []
    for mineral in all_minerals:
        new_color = mineral.color.lower()
        if new_color not in color_list:
            if new_color != '':
                if not re.search('\W', new_color):
                    color_list.append(new_color)
    color_list.sort()
    return {'colors': color_list, }
