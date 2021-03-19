from django.urls import path

from . import views

urlpatterns = [
    path('', views.Sid.as_view()),
]