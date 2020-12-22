from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserReplies
from .serializers import UserRepliesSerializer
from .apps import MeganConfig

# Create your views here.
PREDICTION_ENDPOINT = "https://megan-test-46.herokuapp.com/v1/models/LSTM:predict"

@csrf_exempt
def call(request):
    """
    Function info
    """
    if request == 'GET':
        return

    elif request == 'POST':
        data = MeganConfig.parse(request)
        prediction = requests.post(PREDICTION_ENDPOINT, json=data)
        return prediction.text
