from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('routes', views.routes, name='routes'),
    path('rafting/<slug:rafting_slug>', views.show_rafting, name='rafting'),
]