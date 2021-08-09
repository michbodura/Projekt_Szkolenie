from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig

class ModelszkolenieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelszkolenie'
    verbose_name = 'Baza danych'

class ModelszkolenieAuthConfig(AuthConfig):
    name = 'django.contrib.auth'
    verbose_name = 'Baza danych'