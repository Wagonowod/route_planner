from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Rafting, Things, Images, Timings, Members


def index(request):
    rafting = Rafting.objects.all()
    image = Images.objects.all()
    context = {
        'rafting': rafting,
        'title': 'Планировщик туристических маршрутов',
        'image': image,
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
    image = Images.objects.all().filter()
    timings = Timings.objects.all()
    context = {
        'rafting': rafting,
        'title': rafting.title,
        'content': rafting.content,
        'image': image,
        'timing': timings,
    }

    return render(request, 'rafting/rafting.html', context)


def get_things(request):
    things = Things.objects.all()
    members = Members.objects.all()
    context = {
        'things': things,
        'title': 'Сбор сплава',
        'members': members
    }
    return render(request, 'rafting/things.html', context)
