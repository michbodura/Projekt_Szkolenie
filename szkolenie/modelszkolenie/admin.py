from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User as AuthUser, Group
from .models import User, Company, GaleryImage, Answer, Training, Question, QuestionImage, CompletedTraining
# Register your models here.



class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','tresc','jezyk']
    fieldsets = [
        ('Tresc pytania',               {'fields': ['tresc','jezyk']}),
    ]

class TrainingAdmin(admin.ModelAdmin):
    fields = ['nazwa','czas','obowiazkowe','jezyk']
    list_display = ['nazwa','czas','obowiazkowe','jezyk']
    search_fields = ['nazwa']
    def czas(self, obj: Training) -> str:
        return obj.czas
   

class AnswerAdmin(admin.ModelAdmin):
    fields = ['odp','isCorrect','pytanie']
    list_display = ['pytanie','odp','isCorrect']
    def pytanie(self, obj: Answer) -> str:
        return obj.pytanie.tresc


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dane firmy', {'fields': ['nazwa','adres']})
    ]
    list_display = ['nazwa','adres']
    search_fields = ['nazwa','adres']
    def get_ordering(self,request):
        return ['nazwa']


class UserAdmin(admin.ModelAdmin):
    fields = [('imie','nazwisko'),('email','nrDowodu'),'jezyk','firma']
    list_display = ['firma','imie', 'nazwisko','email','nrDowodu']
    search_fields = ['imie','nazwisko','email','nrDowodu','firma']

    def get_ordering(self,request):
        return ['nazwisko','imie']
   

class CompletedTrainingAdmin(admin.ModelAdmin):
    readonly_fields = ["expiration_date"]
    list_display = ['osoba', 'expiration_date','data_ukonczenia', 'szkolenie']
    fieldsets = [
        ('Dane osobowe',               {'fields': ['osoba','szkolenie']}),
        ('Ukonczone szkolenie',               {'fields': ['data_ukonczenia','expiration_date']}),
    ]
    def expiration_date(self, obj: CompletedTraining) -> str:
        return obj.expiration_date
    expiration_date.short_description = 'Data wygaśnięcia'
    def get_ordering(self,request):
        return ['-data_ukonczenia']



class GaleryImageAdmin(admin.ModelAdmin):
    list_display = ["id","tytul","date","szkolenie"]
    def get_ordering(self,request):
        return ['-date']

class QuestionImageAdmin(admin.ModelAdmin):

    list_display = ["tytul","date"]
    def get_ordering(self,request):
        return ['-date']

class MyAdminSite(AdminSite):
    site_header = 'Panel administracyjny do obsługi szkoleń'
    site_title = 'Portal administracyjny do obsługi szkoleń'
    index_title = 'Witamy w panelu administracyjnym do obsługi szkoleń'


my_admin_site = MyAdminSite(name='admin')
    
my_admin_site.register(User, UserAdmin)
my_admin_site.register(Company, CompanyAdmin)
my_admin_site.register(Training,TrainingAdmin)
my_admin_site.register(Question, QuestionAdmin)
my_admin_site.register(Answer,AnswerAdmin)
my_admin_site.register(GaleryImage,GaleryImageAdmin)
my_admin_site.register(QuestionImage, QuestionImageAdmin)
my_admin_site.register(CompletedTraining,CompletedTrainingAdmin)
my_admin_site.register(AuthUser)
my_admin_site.register(Group)
