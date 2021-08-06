from django.contrib import admin

from .models import User, Company, GaleryImage, Answer, Training, Question, QuestionImage
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['tresc','jezyk']

class TrainingAdmin(admin.ModelAdmin):
    fields = ['nazwa','poczatek','czas','obowiazkowe','jezyk','uczestnicy']

class AnswerAdmin(admin.ModelAdmin):
    fields = ['odp','isCorrect','pytanie']

class GaleryImageAdmin(admin.ModelAdmin):
    fields = ['tytul','obraz','date','szkolenie']

class QuestionImageAdmin(admin.ModelAdmin):
    fields = ['tytul','obraz','date','pytanie']

class CompanyAdmin(admin.ModelAdmin):
    fields = ['nazwa','adres']

admin.site.register(User)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Training,TrainingAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(GaleryImage,GaleryImageAdmin)
admin.site.register(QuestionImage,QuestionImageAdmin)



