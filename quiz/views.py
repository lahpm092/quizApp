from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
from .forms import multipleChoice
from .models import Quiz, Question, Answer

def index(request):
    quiz_list = Quiz.objects.all()
    context = {'quizzes': quiz_list}
    return render(request, 'quiz/index.html', context)

def quiz_page(request):
    if request.method == 'POST':
        form = multipleChoice(request.POST)
        if form.is_valid():
            picked = form.cleaned_data.get('picked')
    else:
        form = multipleChoice
    return render(request,'quiz/quiz_page.html', {'form':form})
