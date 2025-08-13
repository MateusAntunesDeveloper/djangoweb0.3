from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views


urlpatterns = [
    path("polls/", views.tarefas, name='polls'),
    path("create_account/",views.Creat),
    path("polls/API/", views.api_key_front_javascript_futureTS, name="api_example"),
]