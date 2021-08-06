from django.contrib import admin

from .models import User, Company, GaleryImage, Answer, Training, Question, QuestionImage, CompletedTraining
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['tresc','jezyk']
    list_display = ['id','tresc','jezyk']

class TrainingAdmin(admin.ModelAdmin):
    fields = ['nazwa','czas','obowiazkowe','jezyk','uczestnicy']
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
    list_display = ['expiration_date', 'osoba','szkolenie']

    def expiration_date(self, obj: CompletedTraining) -> str:
        return obj.expiration_date
    expiration_date.short_description = 'Data wygaśnięcia'

class GaleryImageAdmin(admin.ModelAdmin):
    list_display = ["id","tytul","date","szkolenie"]

class QuestionImageAdmin(admin.ModelAdmin):
    list_display = ["tytul","date"]

admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Training,TrainingAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(GaleryImage,GaleryImageAdmin)
admin.site.register(QuestionImage, QuestionImageAdmin)
admin.site.register(CompletedTraining,CompletedTrainingAdmin)
