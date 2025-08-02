from django.shortcuts import render, redirect
from .models import Question, Result
from django.http import JsonResponse
from django.utils import timezone

def home(request):
    return render(request, 'quizapp/home.html')

def start_quiz(request):
    username = request.POST.get('username')
    request.session['username'] = username
    questions = list(Question.objects.all())
    return render(request, 'quizapp/quiz.html', {'questions': questions})

def submit_quiz(request):
    questions = Question.objects.all()
    score = 0
    for q in questions:
        selected = request.POST.get(str(q.id))
        if selected and int(selected) == q.correct_option:
            score += 1
    username = request.session.get('username', 'Anonymous')
    Result.objects.create(username=username, score=score)
    return render(request, 'quizapp/result.html', {'score': score, 'total': questions.count()})
