from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Rafting, Things


def index(request):
    rafting = Rafting.objects.all().prefetch_related('images')
    context = {
        'rafting': rafting,
        'title': 'Планировщик туристических маршрутов',
    }
    return render(request, 'rafting/index.html', context)


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

def get_things(request):
    things = Things.objects.all()
    context = {
        'things': things,
        'title': 'Сбор сплава',
    }
    return render(request, 'rafting/things.html', context)
