from django.apps import AppConfig
from .preprocessing import PreProcess

class MeganConfig(AppConfig):
    name = 'Megan'
    parse = PreProcess