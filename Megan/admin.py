from django.contrib import admin

from .models import Replies
from .models import UserData

# Register your models here.
admin.site.register(Replies)
admin.site.register(UserData)
