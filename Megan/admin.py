from django.contrib import admin

from .models import Replies, UserData, NewDataset

# Register your models here.
admin.site.register(Replies)
admin.site.register(UserData)
admin.site.register(NewDataset)
