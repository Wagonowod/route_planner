from django.shortcuts import render, get_object_or_404
from .models import Rafting, Things, Images, Timings


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
    timings = Timings.objects.order_by('order')
    dayss = []
    days = []
    for time in timings:
        dayss.append(time.day)
    dayss = sorted(list(set(dayss)))
    for day in dayss:
        days.append({'day': day, 'timings': list(filter(lambda timing: (timing.day == day), timings))})
    context = {
        'rafting': rafting,
        'title': rafting.title,
        'content': rafting.content,
        'image': image,
        'days': days,
    }

    return render(request, 'rafting/rafting.html', context)


def get_things(request):
    things = Things.objects.all()
    context = {
        'title': 'Снаряжение',
        'things': things

    }
    return render(request, 'rafting/things.html', context)
