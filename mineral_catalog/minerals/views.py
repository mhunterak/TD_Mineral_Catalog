import random

from django.contrib import messages
from django.shortcuts import render, redirect

from minerals.models import Mineral


# Create your views here.
def mineral_list(request):
    '''This function is the view for showing the complete mineral list'''
    minerals = Mineral.objects.all()
    # if no minerals are present in the database, load them from json
    if minerals.count() == 0:
        Mineral.load_from_json()
    return render(
        request,
        'index.html',
        {'minerals': minerals, },
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
        {'mineral': mineral, 'kv_list': mineral.kv_list(), }
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
