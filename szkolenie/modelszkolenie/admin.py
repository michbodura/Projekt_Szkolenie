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


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('_my_field',)
    readonly_fields = ('_my_field', )     

    def _my_field(self, obj):
        return obj.get_full_name()
    _my_field.short_description = 'my custom label'