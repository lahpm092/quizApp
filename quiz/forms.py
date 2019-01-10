from django import forms
from .models import Quiz


class multipleChoice(forms.Form):
    choices = Quiz.objects.all()
    CHOICES = []
    for choice in choices:
        CHOICES.append((choice.topic, choice.topic))
    picked = forms.MultipleChoiceField(choices=CHOICES, \
    widget=forms.Select())
