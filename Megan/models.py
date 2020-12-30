from django.db import models

# Create your models here.

class Replies(models.Model):
    stage = models.IntegerField()
    response_type = models.CharField(max_length=10)
    text = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=10)