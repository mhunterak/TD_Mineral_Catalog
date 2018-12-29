import json
import os

from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render

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
        {'mineral': mineral}
    )


def load_new_minerals(request):
    with open('./assets/minerals.json', 'r') as f:
        print('================')
        print(str(f))
        print('================')
        j = json.loads(str(f))

        pass


def home(request):
    return render(
        request,
        'index.html')
