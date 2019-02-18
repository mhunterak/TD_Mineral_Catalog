import string
from .forms import SearchForm
from .static_vars import GROUPS

def search_form(request):
    return {
        'SearchForm': SearchForm()
    }


def alphabet(request):
    return {
        'alphabet': string.ascii_uppercase,
    }


def groups(request):
    return {'groups': GROUPS,}
