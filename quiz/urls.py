from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions_form/', views.questions_form, name='quesions_form'),
    path('questions_save/', views.questions_save, name='quesions_save'),
    path('display_questions/', views.display_questions, name='display_questions'),
    path('hitOrMiss/', views.hitOrMiss, name='hitOrMiss'),
]
