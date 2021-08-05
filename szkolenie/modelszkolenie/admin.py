from django.contrib import admin
from .models import Gosc, Firma, ObrazDoGalerii, Odpowiedz, Szkolenie, Pytanie
# Register your models here.
admin.site.register(Gosc)
admin.site.register(Firma)
admin.site.register(Szkolenie)
admin.site.register(Pytanie)
admin.site.register(Odpowiedz)
admin.site.register(ObrazDoGalerii)
 