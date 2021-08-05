from django.db import models
from django.db.models.base import ModelState
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Company(models.Model):
    nazwa = models.CharField(max_length=60)
    adres = models.CharField(max_length=120)

    class Meta: 
        verbose_name_plural = "Firma"

class Language(models.TextChoices):
    ENGLISH = 'EN', _('English')
    POLISH = 'PL', _('Polish')


class User(models.Model):
    
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nrDowodu = models.CharField(max_length=15,null=True)
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True
    )

    firma = models.ForeignKey(
        Company, 
        related_name='companies',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )




    class Meta:
        verbose_name_plural="Gość"

class Training(models.Model):
    nazwa = models.CharField(max_length=100)
    poczatek = models.DateTimeField(blank=True, null=True)
   
    koniec = models.DateTimeField(blank=True, null=True)
    obraz = models.ImageField(upload_to="images/szkolenie")
    
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True
    )
    listCustomers = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural="Szkolenie"
    
    def date_diff(self):
        return (self.koniec- self.obraz)
    
    print(date_diff)


class Question(models.Model):
    tresc = models.TextField()
    obraz = models.ImageField()
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural="Pytanie"

class Answer(models.Model):
    odpPopr = models.CharField(max_length=20)
    odpNiepopr = models.CharField(max_length=20)
    pytanie = models.OneToOneField(
        Question, 
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    class Meta:
        verbose_name_plural = "Odpowiedź"

class GaleryImage(models.Model):
    
    tytul = models.CharField(max_length=100)
    obraz = models.ImageField(upload_to="images/szkolenie/galeria")
    data = models.DateTimeField(auto_now_add=True)
    szkolenie = models.ForeignKey(
        Training, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = "Galeria"
        ordering = ['-data']