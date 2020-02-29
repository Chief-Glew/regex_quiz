from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic

from quiz.forms import AnswerForm, QuizForm, QuestionForm
from quiz.models import Quiz, Question
from regex.regex import check_regex_equivalent


def index(request):
    return render(request, 'quiz/index.html')


def quizzes(request):
    context = {
        'quizzes': Quiz.objects.all()
    }
    return render(request, 'quiz/quizzes.html', context)


def do_quiz(request, quiz_id, question_id=0):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    context = {
        'quiz': quiz,
    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswerForm(request.POST)
        question = get_object_or_404(Question, pk=question_id)
        if form.is_valid():
            attempt = form.cleaned_data['answer']
            correct, expected, actual = check_regex_equivalent(quiz.quiz_text, question.answer, attempt)
            context['correct'] = correct
            context['expected'] = expected
            context['actual'] = actual

    # if a GET (or any other method) we'll create a blank form and get the next question
    else:
        form = AnswerForm()
        question = quiz.question_set.filter(pk__gt=question_id).first()
        if question is None:
            return redirect('quiz:quizzes')

    context['form'] = form
    context['question'] = question
    return render(request, 'quiz/do_quiz.html', context)


def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('quiz:add_question', quiz.id)
    else:
        form = QuizForm()

    return render(request, 'quiz/add_quiz.html', {'form': form})


def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    context = {
        'quiz': quiz
    }
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            if form.cleaned_data['add_another']:
                return redirect('quiz:add_question', quiz.id)
            else:
                return redirect('quiz:quiz', quiz_id)
    else:
        form = QuestionForm(initial={'quiz': quiz})

    context['form'] = form
    return render(request, 'quiz/add_question.html', context)


class QuizView(generic.DetailView):
    model = Quiz
    template_name = 'quiz/quiz.html'
