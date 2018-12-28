from django.shortcuts import render
from django.http import HttpResponse

from minerals.models import Mineral


# Create your views here.
def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(
        request,
        'minerals/minerals_list.html',
        {'minerals': minerals, },
    )


def hello_world(request):
    return HttpResponse('Hello World')
