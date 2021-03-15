import numpy as np

import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sid.models import Record

PREDICTION_ENDPOINT = "https://socialmediamonitor.herokuapp.com/v1/models/bert:predict"


@csrf_exempt
def index(request):
    if request.method == 'GET':
        parsed = {
            "instances": ["Wake up!"]
        }
        response = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = json.loads(response.text)['predictions'][0]
        if result:
            return JsonResponse("Success!", safe=False)
        else:
            return JsonResponse("Prediction service offline!", safe=False)

    elif request.method == 'POST':
        text = request.POST['text']
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
