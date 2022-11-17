from django.shortcuts import render
from django.http import HttpResponse
from .models import Rafting_23

def index(request):
    return render(request, 'rafting/index.html')


def routes(request):
    rafting = Rafting_23.objects.all()
    context = {
        'rafting': rafting,
        'title' : 'Маршруты',
    }
    return render(request, 'rafting/routes.html', context)


def get_rafting(request, id):
    rafting = Rafting_23.objects.get(pk=id)
    context = {
        'rafting': rafting,

    }
    return render(request, 'rafting/rafting.html', context)
