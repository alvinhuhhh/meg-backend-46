import json
import requests
from .preprocessing import PreProcess
from .preprocessing import ProcessResult

PREDICTION_ENDPOINT = "https://megan-test-46.herokuapp.com/v1/models/LSTM:predict"

class Handler:

    def one(self, body=None):
        return "Hey! I'm Megan!"

    def two(self, body=None):
        return "What's your name?"

    def three(self, body=None):
        return "Hi User! So how you feeling today?"

    def four(self, body=None):
        parsed = PreProcess(body["text"])
        predictions = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = ProcessResult(predictions.text)
        if result == 0:
            return "Aiyo why liddat? Its okay sometimes I feel liddat also..."
        elif result == 4:
            return "Swee! I see you happy I also shiok!"
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
        except:
            return "Out of bounds!"
        
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