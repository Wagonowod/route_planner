from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Rafting


def index(request):
    return render(request, 'rafting/index.html')


def routes(request):
    rafting = Rafting.objects.all()
    context = {
        'rafting': rafting,
        'title': 'Маршруты',
    }
    return render(request, 'rafting/routes.html', context)


def show_rafting(request, rafting_slug):
    rafting = get_object_or_404(Rafting, slug=rafting_slug)

    context = {
        'rafting': rafting,
        'title': rafting.title,
        'content': rafting.content
    }

    return render(request, 'rafting/rafting.html', context)
