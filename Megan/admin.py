from django.contrib import admin

from .models import Replies
from .models import UserMessages

# Register your models here.
admin.site.register(Replies)
admin.site.register(UserMessages)
