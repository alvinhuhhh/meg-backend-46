from django.db import models

# Create your models here.


class Replies(models.Model):
    stage = models.IntegerField()
    response_type = models.CharField(max_length=50)
    text = models.TextField()
    sentiment = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class UserMessages(models.Model):
    _id = models.IntegerField()
    stage = models.IntegerField()

    def __str__(self):
        return self.text
