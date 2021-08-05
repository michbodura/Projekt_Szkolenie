from django.db import models
from django.db.models.base import ModelState
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Firma(models.Model):
    nazwa = models.CharField(max_length=60)
    adres = models.CharField(max_length=120)

    class Meta: 
        verbose_name_plural = "Nazwa"

class Jezyk(models.TextChoices):
    ENGLISH = 'EN', _('English')
    POLISH = 'PL', _('Polish')


class Gosc(models.Model):
    
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nrDowodu = models.IntegerField(blank=True, null=True)
    jezyk = models.CharField(
        max_length=2,
        choices=Jezyk.choices,
        blank=True,
        null=True
    )

    firma = models.OneToOneField(
        Firma, 
        on_delete=models.CASCADE,
        blank=True, null=True,
    )




    class Meta:
        verbose_name_plural="Gość"

class Szkolenie(models.Model):
    nazwa = models.CharField(max_length=100)
    data = models.DateField()
    obraz = models.ImageField(upload_to="images/szkolenie")
    
    jezyk = models.CharField(
        max_length=2,
        choices=Jezyk.choices,
        blank=True,
        null=True
    )
    lista_gosci = models.ManyToManyField(Gosc)

    class Meta:
        verbose_name_plural="Szkolenie"


class Pytanie(models.Model):
    tresc = models.TextField()
    obraz = models.ImageField()
    jezyk = models.CharField(
        max_length=2,
        choices=Jezyk.choices,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural="Pytanie"

class Odpowiedz(models.Model):
    odpPopr = models.CharField(max_length=20)
    odpNiepopr = models.CharField(max_length=20)
    pytanie = models.OneToOneField(
        Pytanie, 
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    class Meta:
        verbose_name_plural = "Odpowiedź"

class ObrazDoGalerii(models.Model):
    
    tytul = models.CharField(max_length=100)
    obraz = models.ImageField(upload_to="images/szkolenie/galeria")
    data = models.DateField()
    szkolenie = models.ForeignKey(
        Szkolenie, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = "Galeria"