from django.shortcuts import render
from django.http import HttpResponse
from . import urls

def tarefass(request):

    return HttpResponse("ola mundosssss")


def index(request):
    return render(request, "index.html")
    
def Create_account(request):
    return render(request,"create_acc.html")
def prod1(request):
    return render(request, "prod1.html")
    