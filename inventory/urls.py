from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('add', views.add_view, name='add_file'),
]