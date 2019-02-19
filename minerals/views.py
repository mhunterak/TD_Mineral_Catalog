'''

Mineral Catalog: Views

-----------------
Table of Contents
-----------------

- List views
    Filters
    Queries
- Details views

'''
import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from minerals.models import Mineral


# LIST VIEWS
#   FILTERS


def mineral_list(request):
    '''
This function is the view for showing the complete mineral list

for project 8, this view redirects to the letter filter for "A"
    '''
    return redirect('filter', query="A")


def all_minerals(request):
    '''
This function is the view for showing the complete mineral list
    '''
    minerals = Mineral.objects.all()
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
        },
    )


#   QUERIES


def filter_by_first_letter(request, query):
    '''
This function is the view for showing a filtered mineral list by 
the first letter of the name
    '''
    # get minerals with a specific color in the color field
    minerals = Mineral.objects.filter(name__startswith=query)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'letter': query.upper(),
        },
    )


def filter_by_group(request, query):
    '''
This function is the view for showing a filtered mineral list by
the Mineral's group attribute
    '''
    minerals = Mineral.objects.filter(group=query)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'group': query,
        },
    )


def filter_by_color(request, query):
    '''
This function is the view for showing a list of minerals with a specific color
in the color field.
    '''
    # get minerals with a specific color in the color field
    minerals = Mineral.objects.filter(color__contains=query)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'color_listing': query,
        },
    )


''' DEPRECATED
switched this to search all values,
def mineral_name_search(request):
    if request.POST:
        query = request.POST['search']
    else:
        query = ""
    minerals = Mineral.objects.filter(name__contains=query)
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'query': query,
        },
    )
'''


def mineral_all_search(request):
    '''
This function is the view for the extra credit requirement that applys the
search query to every field, not just the name (DEPRECATED)

developed from this helpful stack overflow post:
from https://stackoverflow.com/questions/1866847/searching-all-fields-in-a-table-in-django
    '''
    if request.POST:
        # save the primary key
        query = request.POST['search']
    else:
        # if this view is called without a query, show all minerals
        return redirect('all')

    or_query = None
    for field_name in Mineral.iter():
        q = Q(**{"%s__contains" % field_name: query})
        if or_query is None:
            or_query = q
        else:
            or_query = or_query | q
    minerals = Mineral.objects.filter(or_query)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'query': query,
        },
    )


# DETAIL VIEWS


def random_mineral(request):
    '''
This function is the view for selecting a random mineral
    '''
    # generate random number between 1 and the number of minerals we have
    random_id = random.randint(1, Mineral.objects.count())
    # return a redirect the detail page for that mineral
    return redirect('/detail/{}'.format(random_id))


def mineral_detail(request, pk):
    '''
This function is the view for showing a specific mineral in detail
    '''
    try:
        mineral = Mineral.objects.get(pk=pk)
    except Mineral.DoesNotExist:
        messages.add_message(
            request,
            messages.INFO,
            "We couldn't find a mineral for that ID. Please pick a new one: ")
        return redirect('/')
    return render(
        request,
        'detail.html',
        {
            'mineral': mineral,
            'kv_list': mineral.kv_list(),
        }
    )
