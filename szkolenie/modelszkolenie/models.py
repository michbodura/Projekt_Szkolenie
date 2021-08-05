from django.db import models
from django.db.models.base import ModelState
from django.utils.translation import gettext_lazy as _
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import datetime

# Create your models here.

class Company(models.Model):
    nazwa = models.CharField(max_length=60)
    adres = models.CharField(max_length=120)

    class Meta: 
        verbose_name_plural = "Firma"
    
    def __str__(self):
        return self.nazwa

class Language(models.TextChoices):
    ENGLISH = 'EN', _('Angielski')
    POLISH = 'PL', _('Polski')


class User(models.Model):
    
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nrDowodu = models.CharField(max_length=26,null=True)
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

    def __str__(self):
        return self.imie + " " + self.nazwisko

    class Meta:
        verbose_name_plural="Gość"
    
class Training(models.Model):
    nazwa = models.CharField(max_length=255)
    poczatek = models.DateField(blank=True, null=True)
   
    czas = models.DurationField(verbose_name="czas")
    obraz = models.ImageField(upload_to="images/szkolenie")
    
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True
    )
    uczestnicy = models.ManyToManyField(User, blank=True)

    class Meta:
        verbose_name_plural="Szkolenie"

    def __str__(self):
        return self.nazwa

  
    @property
    def expiration_date(self):
        return (self.poczatek + self.czas)

    




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
    odp = models.TextField()
    isCorrect = models.BooleanField(default=False)
    pytanie = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    def __str__(self):
        return self.odp
    class Meta:
        verbose_name_plural = "Odpowiedź"

class GaleryImage(models.Model):
    
    tytul = models.CharField(max_length=255)
    obraz = models.ImageField(upload_to="images/szkolenie/galeria")
    date = models.DateTimeField(auto_now_add=True)
    szkolenie = models.ForeignKey(
        Training, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.tytul
    class Meta:
        verbose_name_plural = "Galeria"
        ordering = ['-date']

class QuestionImage(models.Model):
    tytul = models.CharField(max_length=255)
    obraz = models.ImageField(upload_to="images/szkolenie/galeria")
    date = models.DateTimeField(auto_now_add=True)
    pytanie = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.tytul
    class Meta:
        verbose_name_plural = "Galeria pytan"
        ordering = ['-date']