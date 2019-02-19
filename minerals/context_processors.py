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


def colors(request):
    color_list = []
    for mineral in Mineral.objects.all():
        if mineral.color not in color_list:
            if mineral.color != '':
                if not re.search('\W', mineral.color):
                    color_list.append(mineral.color)
    color_list.sort()
    return {'colors': color_list, }
