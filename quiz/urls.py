from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('quizzes', views.quizzes, name='quizzes'),
    path('quiz/<int:pk>', views.QuizView.as_view(), name='quiz'),
    path('do_quiz/<int:quiz_pk>', views.do_quiz, name='do_quiz'),
    path('do_quiz/<int:quiz_pk>/<int:last_question>', views.do_quiz, name='do_quiz'),
]
