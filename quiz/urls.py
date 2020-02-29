from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('quizzes', views.quizzes, name='quizzes'),
    path('quiz/<int:pk>', views.QuizView.as_view(), name='quiz'),
    path('do_quiz/<int:quiz_id>', views.do_quiz, name='do_quiz'),
    path('do_quiz/<int:quiz_id>/<int:question_id>', views.do_quiz, name='do_quiz'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('add_question/<int:quiz_id>', views.add_question, name='add_question'),
]

