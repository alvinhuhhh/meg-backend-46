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
    name = models.TextField(default='user', max_length=50)
    user_id = models.IntegerField(primary_key=True)
    stage = models.IntegerField()
    messages = ArrayField(models.CharField(max_length=100, blank=True))

    def __str__(self):
        return self.name


class NewDataset(models.Model):
    _id = models.IntegerField(default=0)
    sentence = models.TextField(default='')
    sentiment = models.IntegerField(default=9)

    def _str__(self):
        return self._id
