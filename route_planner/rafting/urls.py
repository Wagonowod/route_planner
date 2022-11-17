from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('routes', views.routes, name='routes'),
    path('rafting/<int:id>', views.get_rafting, name='detail'),
]