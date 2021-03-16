import json
import requests
from .models import Replies, UserData, NewDataset

PREDICTION_ENDPOINT = "https://megan-bert-v4.herokuapp.com/v1/models/meganBERTv4:predict"


class Handler:

    def one(self, body=None):
        return Replies.objects.get(stage=1).text

    def two(self, body=None):
        return Replies.objects.get(stage=2).text

    def three(self, body=None):
        # Get username from body
        username = body["text"]
        # Save username in database
        user = UserData.objects.get(user_id=int(body["user_id"]))
        user.name = username
        user.save(force_update=True)
        # Get appropriate response from database
        db_text = Replies.objects.get(stage=3).text
        # Replace placeholder with username
        txt = db_text.replace("User", username)

        return txt

    def four(self, body=None):
        # Save user's reply to NewDataset
        new = NewDataset(
            _id=body["user_id"],
            sentence=body["text"],
            sentiment=9  # Default
        )
        new.save()
        # Parse and send user's reply to prediction endpoint
        parsed = {
            "instances": [body["text"]]
        }
        JsonResponse = requests.post(PREDICTION_ENDPOINT, json=parsed)
        result = json.loads(JsonResponse.text)['predictions'][0][0]
        # Classify and get appropriate response from database
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
        # Get sentiment rating from body
        sentiment = int(body["text"])
        # Get the correct sentence by _id from database
        sentence = NewDataset.objects.get(_id=body["user_id"])
        # Update with rated sentiment and save
        sentence.sentiment = sentiment
        sentence.save(force_update=True)

        return Replies.objects.get(stage=6).text

    def seven(self, body=None):
        return Replies.objects.get(stage=7).text

    def OutOfBounds(self, body=None):
        return 'Integer stage out of bounds!'

    stages = {
        "1": one,
        "2": two,
        "3": three,
        "4": four,
        "5": five,
        "6": six,
        "7": seven,
        "ob": OutOfBounds,
    }

    def handle(self, body):
        """
        Input:
        body(dict)
        Output:
        response(string)
        """
        if body["function"] == "get":
            return "Get messages!"

        elif body["function"] == "message":
            try:
                # If user already exists in database
                if UserData.objects.filter(user_id=int(body["user_id"])):
                    user = UserData.objects.get(
                        user_id=int(body["user_id"])
                    )
                    stage = user.stage
                # Create new user and save in database
                else:
                    new = UserData(
                        name=body["user_id"],
                        user_id=int(body["user_id"]),
                        stage=1,
                        messages=[]
                    )
                    new.save()

                    user = UserData.objects.get(
                        user_id=int(body["user_id"])
                    )
                    stage = user.stage

                # Redirect to switcher to handle different stages
                if stage <= 7:
                    response = self.stages[str(stage)](self, body)
                else:
                    response = self.stages['ob'](self, body)

                # Update database with new stage and message
                if stage < 7:
                    user.stage = stage + 1
                user.messages.append(body["text"])
                user.save()

                return response

            except Exception as e:
                return "Error " + str(e)

        else:
            return "Request failed!"

#########
# Debug #
#########


def main():
    test = {
        "user_id": "1",
        "function": "message",
        "text": "Hello!"
    }
    testHandler = Handler()
    print(testHandler.handle(test))
    return


if __name__ == "__main__":
    main()
