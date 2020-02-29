from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic

from quiz.forms import AnswerForm
from quiz.models import Quiz, Question
from regex.regex import check_regex_equivalent


def index(request):
    return render(request, 'quiz/index.html')


def quizzes(request):
    context = {
        'quizzes': Quiz.objects.all()
    }
    return render(request, 'quiz/quizzes.html', context)


def do_quiz(request, quiz_pk, last_question=0):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    context = {
        'quiz': quiz,
    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswerForm(request.POST)
        question = get_object_or_404(Question, pk=last_question)
        # check whether it's valid:
        if form.is_valid():
            attempt = form.cleaned_data['answer']
            correct, expected, actual = check_regex_equivalent(quiz.quiz_text, question.answer, attempt)
            context['correct'] = correct
            context['expected'] = expected
            context['actual'] = actual

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnswerForm()
        question = quiz.question_set.filter(pk__gt=last_question).first()
        if question is None:
            return redirect('quiz:quizzes')

    context['form'] = form
    context['question'] = question
    return render(request, 'quiz/do_quiz.html', context)


class QuizView(generic.DetailView):
    model = Quiz
    template_name = 'quiz/quiz.html'
