from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .apps import MeganConfig
from .requestHandler import Handler

# Create your views here.


class call_model(APIView):

    def get(self, request, *args, **kwargs):
        return JsonResponse("Success!", safe=False)

    def post(self, request, *args, **kwargs):
        requestHandler = Handler()
        response = requestHandler.handle(request.data)
        return JsonResponse(response, safe=False)
