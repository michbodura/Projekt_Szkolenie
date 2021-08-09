from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User as AuthUser, Group
from .models import User, Company, GaleryImage, Answer, Training, Question, QuestionImage, CompletedTraining
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['tresc','jezyk']
    list_display = ['id','tresc','jezyk']

class TrainingAdmin(admin.ModelAdmin):
    fields = ['nazwa','czas','obowiazkowe','jezyk']
    list_display = ['nazwa','czas','obowiazkowe','jezyk']
    def czas(self, obj: Training) -> str:
        return obj.czas

class AnswerAdmin(admin.ModelAdmin):
    fields = ['odp','isCorrect','pytanie']
    list_display = ['pytanie','odp','isCorrect']
    def pytanie(self, obj: Answer) -> str:
        return obj.pytanie.tresc

class CompanyAdmin(admin.ModelAdmin):
    fields = ['nazwa','adres']
    list_display = ['nazwa','adres']

class UserAdmin(admin.ModelAdmin):
    fields = ['imie','nazwisko','email','nrDowodu','jezyk','firma']
    list_display = ['firma','imie', 'nazwisko','email','nrDowodu']

class CompletedTrainingAdmin(admin.ModelAdmin):
    readonly_fields = ["expiration_date"]
    list_display = ['osoba', 'expiration_date', 'szkolenie']

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


admin_site = MyAdminSite(name='admin')
    
admin_site.register(User, UserAdmin)
admin_site.register(Company, CompanyAdmin)
admin_site.register(Training,TrainingAdmin)
admin_site.register(Question, QuestionAdmin)
admin_site.register(Answer,AnswerAdmin)
admin_site.register(GaleryImage,GaleryImageAdmin)
admin_site.register(QuestionImage, QuestionImageAdmin)
admin_site.register(CompletedTraining,CompletedTrainingAdmin)
admin_site.register(AuthUser)
admin_site.register(Group)

