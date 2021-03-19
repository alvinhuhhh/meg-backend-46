import numpy as np

import requests
import json
from rest_framework.views import APIView
from django.http import JsonResponse

from sid.models import Record

PREDICTION_ENDPOINT = "https://socialmediamonitor.herokuapp.com/v1/models/bert:predict"


class Sid(APIView):
    def get(self, request, *args, **kwargs):
        parsed = {
            "instances": ["Wake up!"]
        }
        response = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = json.loads(response.text)['predictions'][0]
        if result:
            return JsonResponse("Success!", safe=False)
        else:
            return JsonResponse("Prediction service offline!", safe=False)

    def post(self, request, *args, **kwargs):
        text = request.data['text']
        parsed = {
            "instances": [text],
        }
        response = requests.post(PREDICTION_ENDPOINT, json=parsed)
        prediction = json.loads(response.text)['predictions'][0]
        res = np.argmax(prediction)
        new = Record(
            text=text,
            prediction=res,
        )
        new.save()
        return JsonResponse(int(res), safe=False)
