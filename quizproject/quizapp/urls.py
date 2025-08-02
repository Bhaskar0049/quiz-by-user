# quizproject/urls.py
from django.contrib import admin
from django.urls import path
from quizapp import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
]
