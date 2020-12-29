from django.db import models

# Create your models here.
class UserReplies(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class MeganReplies(models.Model):
    num = models.IntegerField()
    stage = models.IntegerField()
    text = models.TextField()
