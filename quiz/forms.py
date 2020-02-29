from django import forms

from quiz.models import Quiz, Question


class AnswerForm(forms.Form):
    answer = forms.CharField(label='answer', max_length=200)


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'quiz_text']
        widgets = {
            'quiz_text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class QuestionForm(forms.ModelForm):
    add_another = forms.BooleanField(required=False)

    class Meta:
        model = Question
        fields = ['question', 'answer', 'quiz']
        widgets = {'quiz': forms.HiddenInput()}

