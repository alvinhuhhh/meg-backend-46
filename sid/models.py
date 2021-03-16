from django.db import models


# Create your models here.


class Record(models.Model):
    text = models.TextField()
    prediction = models.IntegerField()

    def __str__(self):
        return ' '.join(['T:', self.text, 'P:', int(self.prediction)])
