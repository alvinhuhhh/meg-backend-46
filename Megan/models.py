from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Replies(models.Model):
    stage = models.IntegerField()
    response_type = models.CharField(max_length=50)
    text = models.TextField()
    sentiment = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class UserData(models.Model):
    name = models.TextField()
    user_id = models.IntegerField()
    stage = models.IntegerField()
    messages = ArrayField(models.CharField(max_length=100))

    def __str__(self):
        return self.name
