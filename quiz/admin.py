from django.contrib import admin

# Register your models here.
from quiz.models import Question, Quiz

admin.site.register(Quiz)
admin.site.register(Question)
