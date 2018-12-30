import json
import os
import random
import re

from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render, redirect

from minerals.models import Mineral
from mineral_catalog.settings import STATICFILES_DIRS


# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(
        request,
        'minerals/minerals_list.html',
        {'minerals': minerals, },
    )


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(
        request,
        'detail.html',
        {
            'mineral': mineral,
            'kv_list': mineral.kv_list(),
            'keys': mineral.keys(),
            'values': mineral.values(),
        }
    )

def random_mineral(request):
    random_id = random.randint(0, Mineral.objects.count())
    return redirect('/{}_detail/'.format(random_id))

def load_new_minerals(request):
    with open('./assets/minerals.json', 'r') as f:
        json_string = ''
        for line in f:
            json_string += str(line)
        json_list = json.loads(json_string)
        for dict in json_list:
            mineral = Mineral(
                name=dict['name']
            )
            mineral.__dict__.update(dict)
            for key in dict.keys():
                if " " in key:
                    underscore_key = "_".join(key.split(" "))
                    setattr(mineral, underscore_key, dict[key])
            mineral.save()
        return HttpResponse(Mineral.objects.all())


def index(request):
    minerals = Mineral.objects.all()
    return render(
        request,
        'index.html',
        {'minerals': minerals})
