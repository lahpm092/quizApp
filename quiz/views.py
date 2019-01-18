from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
# from .forms import multipleChoice
from .models import Question
from datetime import datetime
from datetime import date
from datetime import timedelta

def index(request):
    question_list = Question.objects.all()
    context = {'questions': question_list}
    return render(request, 'quiz/index.html', context)

def questions_form(request):

    return render(request,'quiz/questions_page.html')

def questions_save(request):
    try:
        question = str(request.POST["question_field"])
        right_answer = str(request.POST["correctAnswer_field"])
        wrong_answer1 = str(request.POST["incorrectAnswer1_field"])
        wrong_answer2 = str(request.POST["incorrectAnswer2_field"])
        wrong_answer3 = str(request.POST["incorrectAnswer3_field"])
    except KeyError:
        return HttpResponse("KeyError")

    q = Question(q = question, right_answer = right_answer, wrong_answer1 \
    = wrong_answer1, wrong_answer2 = wrong_answer2, wrong_answer3 = wrong_answer3)

    q.save()

    return render(request,'quiz/questions_page.html')

def display_questions(request):
    theQuestion = Question.objects.all()[0]
    context = {
        'question': theQuestion.q,
        'right_answer': theQuestion.right_answer,
        'wrong_answer1': theQuestion.wrong_answer1,
        'wrong_answer2': theQuestion.wrong_answer2,
        'wrong_answer3': theQuestion.wrong_answer3,
    }
    return render(request, 'quiz/display_questions.html', context)
