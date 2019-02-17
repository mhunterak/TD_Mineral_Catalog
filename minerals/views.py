import random
import string

from django.contrib import messages
from django.shortcuts import render, redirect

from minerals.models import Mineral


def mineral_list(request):
    '''This function is the view for showing the complete mineral list
    
    for project 8, this view redirects to the letter filter for "A"
    '''
    return redirect('filter', pk="A")
    '''
this is how I did it for project 6, could also be considered a view for 'all' minerals
    minerals = Mineral.objects.all()

    return render(
        request,
        'index.html',
        {'minerals': minerals,
         'alphabet': string.ascii_uppercase },
    )
    '''


def filter_by_first_letter(request, pk):
    '''This function is the view for showing the complete mineral list'''
    minerals = Mineral.objects.filter(name__startswith=pk)
    return render(
        request,
        'index.html',
        {
         'alphabet': string.ascii_uppercase,
         'letter': pk.upper(),
         'minerals': minerals,
         },
    )


def mineral_detail(request, pk):
    '''This function is the view for showing a specific mineral detail view'''
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
            'alphabet': string.ascii_uppercase,
        }
    )


def random_mineral(request):
    '''This function is the view for selecting a random mineral'''
    # generate random number between 1 and the number of minerals we have
    random_id = random.randint(1, Mineral.objects.count())
    # show a message to show that a random mineral was generated
    messages.add_message(
        request,
        messages.INFO,
        "Random Mineral #{}:".format(random_id))

    # return a redirect the detail page for that mineral
    return redirect('/detail/{}'.format(random_id))
