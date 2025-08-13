from django.shortcuts import render

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from . import urls
from django.http import JsonResponse
from rest_framework import status
import requests


class Conection_api_front:

    def test_conection(request):
        return HttpResponse("sucess")
        
    def api_key_front_javascript_futureTS(request):
        data = {
            "message":"BackEnd Response",
            "status":"sucess",
        }
        return JsonResponse(data)


    def error_requestTimeOutInwebServer(request):
        return TimeoutError("<h1 text-3x1 font-normal mb-4 amazom-dark-blue> PageIsNotWorkingGood...</h1>")
    

    def error_404_not_Found(request):      
        try: 
            if HttpResponseNotFound == False:
                JsonResponse.cookies(request)
        except:
            return HttpResponseNotFound("<h1>Not found</h1>")
            