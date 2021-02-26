import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .apps import MeganConfig
from .requestHandler import Handler

# Create your views here.
PREDICTION_ENDPOINT = "https://megan-bert-v4.herokuapp.com/v1/models/meganBERTv4:predict"


class call_model(APIView):

    def get(self, request, *args, **kwargs):
        parsed = {
            "instances": ["Wake up!"]
        }
        response = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = json.loads(response.text)['predictions'][0][0]
        if result:
            return JsonResponse("Success!", safe=False)
        else:
            return JsonResponse("Prediction service offline!", safe=False)

    def post(self, request, *args, **kwargs):
        response = Handler.handle(request.data)
        return JsonResponse(response, safe=False)
