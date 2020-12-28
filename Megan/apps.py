from django.apps import AppConfig
from .preprocessing import PreProcess
from .preprocessing import ProcessResult

class MeganConfig(AppConfig):
    name = 'Megan'
    parse = PreProcess
    decode = ProcessResult