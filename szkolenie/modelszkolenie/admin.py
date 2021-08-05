from django.contrib import admin
from .models import User, Company, GaleryImage, Answer, Training, Question, QuestionImage
# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Training)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(GaleryImage)
admin.site.register(QuestionImage)
 