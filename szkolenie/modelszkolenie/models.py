from django.db import models
from django.utils.translation import gettext_lazy as _

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
    
    imie = models.CharField(max_length=30, verbose_name="Imię")
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nrDowodu = models.CharField(max_length=26,null=True, verbose_name="Numer dowodu")
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True,
        verbose_name="Język"
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
    czas = models.DurationField(verbose_name="czas")
    obowiazkowe = models.BooleanField(default=False, verbose_name="Czy obowiązkowe")
    
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True,
        verbose_name="Język"
    )
    uczestnicy = models.ManyToManyField(User,through='CompletedTraining', blank=True)

    class Meta:
        verbose_name_plural="Szkolenie"

    def __str__(self):
        return self.nazwa

class Question(models.Model):

    tresc = models.TextField(verbose_name="treść")
    jezyk = models.CharField(
        max_length=2,
        choices=Language.choices,
        blank=True,
        null=True,
        verbose_name="Język"
    )
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural="Pytanie"

class Answer(models.Model):

    odp = models.TextField(verbose_name="Odpowiedź")
    isCorrect = models.BooleanField(default=False, verbose_name="Czy poprawna")
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
    
    tytul = models.CharField(max_length=255, verbose_name="tytuł")
    obraz = models.ImageField(upload_to="images/szkolenie/galeria")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Data wstawienia")
    szkolenie = models.ForeignKey(
        Training, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.tytul
    class Meta:
        verbose_name_plural = "Galeria ze szkolenia"
        ordering = ['-date']

class QuestionImage(models.Model):

    tytul = models.CharField(max_length=255, verbose_name="tytuł")
    obraz = models.ImageField(upload_to="images/pytanie/galeria")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Data")
    pytanie = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.tytul
    class Meta:
        verbose_name_plural = "Galeria pytan na szkoleniu"
        ordering = ['-date']

class CompletedTraining(models.Model):

    osoba = models.ForeignKey(User, on_delete=models.CASCADE)
    szkolenie = models.ForeignKey(Training, on_delete=models.CASCADE)
    data_ukonczenia = models.DateField(blank=True, null=True,verbose_name="Data ukończenia")

    @property
    def expiration_date(self):
        return (self.data_ukonczenia + self.szkolenie.czas)

    class Meta:
        verbose_name_plural = "Ukonczone szkolenia"

    
