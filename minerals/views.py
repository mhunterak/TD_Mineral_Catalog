import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, reverse

from minerals.models import Mineral


#   LIST VIEWS


def index(request):
    '''
This function is the view for:
showing the complete mineral list

for project 8, this view redirects to the letter filter for "A"
    '''
    return redirect('filter', query="A")


def all_minerals(request):
    '''
This function is the view for showing the complete mineral list
just in case you want to
    '''
    minerals = Mineral.objects.all()
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'count': len(minerals),
        },
    )


#   FILTER VIEWS


def filter_by_first_letter(request, query):
    '''
This function is the view for:
showing a filtered mineral list by the first letter of the name
    '''
    # get minerals with a specific color in the color field
    minerals = Mineral.objects.filter(name__startswith=query)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'count': len(minerals),
            'letter': query.upper(),
        },
    )


def filter_by_group(request, query):
    '''
This function is the view for:
showing a filtered mineral list by the Mineral's group attribute
    '''
    minerals = Mineral.objects.filter(group=query)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'count': len(minerals),
            'group': query,
        },
    )


def filter_by_color(request, query):
    '''
This function is the view for:
showing a list of minerals with a specific color in the color field.
    '''
    q = Q(color__icontains=query)
    if query == 'grey':
        q = q | Q(color__icontains='gray')
    if query == 'colorless':
        q = q | Q(color__icontains='colourless')
    # get minerals with a specific color in the color field
    minerals = Mineral.objects.filter(q)
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'count': len(minerals),
            'color_listing': query,
        },
    )


#   SEARCH VIEWS


''' DEPRECATED - switched this to search all values
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
This function is the view for:
the extra credit requirement that applys the search query to every field,
not just the name (see DEPRECATED, prev function)
    '''
    # developed from this helpful stack overflow post:
    # https://stackoverflow.com/questions/1866847/searching-all-fields-in-a-table-in-django
    if request.POST:
        # save the primary key
        query = request.POST['search']
    else:
        # if this view is called without a query, show all minerals
        return redirect('all')

    or_query = None
    for field_name in Mineral.iter_attr():
        # for every searchable field, add to the query
        # uses django's Q object to combine queries into one
        # individual queries are q, the combined query is or_query
        q = Q(**{"%s__icontains" % field_name: query})
        if or_query is None:
            or_query = q
        else:
            or_query = or_query | q
    # get the query from the combined Q query object
    minerals = Mineral.objects.filter(or_query).annotate()
    # render the list template with the queried minerals
    return render(
        request,
        'list.html',
        {
            'minerals': minerals,
            'count': len(minerals),
            'query': query,
        },
    )


#   DETAIL VIEWS


def random_mineral(request):
    '''
This function is the view for:
selecting a random mineral
    '''
    # generate random number between 1 and the number of minerals we have
    random_id = random.randint(1, Mineral.objects.count())
    # return a redirect the detail page for that mineral
    return redirect('minerals:detail', pk=random_id)


def mineral_detail(request, pk):
    '''
This function is the view for:
showing a specific mineral in detail
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
