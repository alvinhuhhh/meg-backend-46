import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .apps import MeganConfig

# Create your views here.
PREDICTION_ENDPOINT = "https://megan-test-46.herokuapp.com/v1/models/LSTM:predict"

class call_model(APIView):

    def get(self, request, *args, **kwargs):
        return JsonResponse("Hello! I'm Megan!", safe=False)
    
    def post(self, request, *args, **kwargs):
        parsed = MeganConfig.parse(str(request.data['text']))
        prediction = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = MeganConfig.decode(prediction.text)
        return JsonResponse(str(result), safe=False)
