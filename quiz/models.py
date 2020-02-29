from django.db import models


class Quiz(models.Model):
    quiz_text = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)