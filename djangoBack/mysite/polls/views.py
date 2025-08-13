from django.shortcuts import render
from django.urls import path
# Create your views here.
from django.http import HttpResponse
from . import views


def index(request):
    return HttpResponse("Hello world. You're at the polls index.")

urlpatterns = [
    path("", views.index, name="index"),
]