import json
import requests
from .preprocessing import PreProcess
from .preprocessing import ProcessResult
from .models import Replies

PREDICTION_ENDPOINT = "https://megan-test-46.herokuapp.com/v1/models/LSTM:predict"

class Handler:

    def one(self, body=None):
        return Replies.objects.get(stage=1).text

    def two(self, body=None):
        return Replies.objects.get(stage=2).text

    def three(self, body=None):
        return Replies.objects.get(id=3).text

    def four(self, body=None):
        parsed = PreProcess(body["text"])
        predictions = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = ProcessResult(predictions.text)
        if result == 0:
            return Replies.objects.get(id=8).text
        elif result == 4:
            return Replies.objects.get(id=4).text
        else:
            return "Error!"

    stages = {"1": one, "2": two, "3": three, "4": four}

    def handle(self, body):
        """
        Input:
        body(dict)
        Output:
        response(string)
        """
        try:
            response = self.stages.get(body["stage"])
            return response(self, body)
        except Exception as e:
            return "Error: " + str(e) 
        
#########
# Debug #
#########
def main():
    test = {
        "id": "1",
        "stage": "4",
        "type": "OE Response",
        "text": "i am sad @alvinhuhhh"
    }
    testHandler = Handler()
    print(testHandler.handle(test))
    return

if __name__ == "__main__":
    main()