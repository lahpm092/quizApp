from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz_page/', views.quiz_page, name='quiz_page'),
]
