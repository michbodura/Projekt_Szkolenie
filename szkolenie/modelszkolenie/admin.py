from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User as AuthUser, Group
from .models import User, Company, GaleryImage, Answer, Training, Question, QuestionImage, CompletedTraining
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['tresc','jezyk']
    list_display = ['id','tresc','jezyk']

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    fields = ['nazwa','czas','obowiazkowe','jezyk']
    list_display = ['nazwa','czas','obowiazkowe','jezyk']
    def czas(self, obj: Training) -> str:
        return obj.czas

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ['odp','isCorrect','pytanie']
    list_display = ['pytanie','odp','isCorrect']
    def pytanie(self, obj: Answer) -> str:
        return obj.pytanie.tresc

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dane osobowe', {'fields': ['nazwa','adres']})
    ]
    list_display = ['nazwa','adres']

class UserAdmin(admin.ModelAdmin):
    fields = ['imie','nazwisko','email','nrDowodu','jezyk','firma']
    list_display = ['firma','imie', 'nazwisko','email','nrDowodu']

class CompletedTrainingAdmin(admin.ModelAdmin):
    readonly_fields = ["expiration_date"]
    list_display = ['osoba', 'expiration_date', 'szkolenie']
    fieldsets = [
        ('Dane osobowe',               {'fields': ['osoba','szkolenie']}),
        ('Ukonczone szkolenie',               {'fields': ['data_ukonczenia','expiration_date']}),
    ]
    def expiration_date(self, obj: CompletedTraining) -> str:
        return obj.expiration_date
    expiration_date.short_description = 'Data wygaśnięcia'



class GaleryImageAdmin(admin.ModelAdmin):
    list_display = ["id","tytul","date","szkolenie"]

class QuestionImageAdmin(admin.ModelAdmin):

    list_display = ["tytul","date"]

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
