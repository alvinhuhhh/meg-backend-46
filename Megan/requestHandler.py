import json
import requests
from .models import Replies

PREDICTION_ENDPOINT = "https://megan-bert-v4.herokuapp.com/v1/models/meganBERTv4:predict"


class Handler:

    def one(self, body=None):
        return Replies.objects.get(stage=1).text

    def two(self, body=None):
        return Replies.objects.get(stage=2).text

    def three(self, body=None):
        return Replies.objects.get(stage=3).text

    def four(self, body=None):
        parsed = {
            "instances": [body["text"]]
        }
        JsonResponse = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = json.loads(JsonResponse.text)['predictions'][0][0]

        if result >= 0.8:
            return Replies.objects.get(stage=4, sentiment='positive').text
        elif result >= 0.01:
            return Replies.objects.get(stage=4, sentiment='neutral').text
        elif result < 0.01:
            return Replies.objects.get(stage=4, sentiment='negative').text
        else:
            return "Error!"

    def five(self, body=None):
        return Replies.objects.get(stage=5).text

    def six(self, body=None):
        return Replies.objects.get(stage=6).text

    def seven(self, body=None):
        return 'Not yet!'

    def eight(self, body=None):
        return 'Not yet!'

    def nine(self, body=None):
        return 'Not yet!'

    stages = {
        "1": one,
        "2": two,
        "3": three,
        "4": four,
        "5": five,
        "6": six,
        "7": seven,
        "8": eight,
        "9": nine,
    }

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
            return "Error!" + e

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
