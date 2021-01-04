from django.db import models

# Create your models here.

class Replies(models.Model):
    stage = models.IntegerField()
    response_type = models.CharField(max_length=10)
    text = models.CharField(max_length=1000)
    sentiment = models.CharField(max_length=10)

    def __str__(self):
        return self.text