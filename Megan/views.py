from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserReplies
from .serializers import UserRepliesSerializer

# Create your views here.
@csrf_exempt
def call(request):
    """
    Function info
    """
    if request == 'GET':
        return

    elif request == 'POST':
        return
