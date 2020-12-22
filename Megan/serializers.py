from rest_framework import serializers
from .models import UserReplies

class UserRepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReplies
        fields = ['text']