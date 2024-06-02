from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from questions.models import Question, Answer
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Quiz
from results.models import Result
from django.contrib.auth.decorators import login_required
from datetime import date

@csrf_exempt
def submit_page(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        quiz_name = request.POST.get('quiz_name')
        quiz = Quiz.objects.filter(name=quiz_name).first()
        user = request.user
        if Result.objects.filter(user=user, quiz=quiz).exists():
            messages.error(request, 'You have already taken this test, You cannot retake!')
            return redirect('profile-view')
        result = Result.objects.create(
            quiz=quiz,
            user=user,
            score=score,
        )
        
        return render(request, 'quizes/profile.html', {'result': result})
    
    return render(request, 'quizes/profile.html')
def profile_page(request):
    results = Result.objects.all()
    courses = Quiz.objects.all()
    return render(request, 'quizes/profile.html', {'results': results, 'courses': courses, 'today': date.today()})
def results_page(request):
    score = request.GET.get('score')
    total = request.GET.get('total')
    if score is None or total is None:
        return HttpResponse("Invalid request")
    try:
        score = int(score)
        total = int(total)
    except ValueError:
        return HttpResponse("Invalid parameters")
    return render(request, 'quizes/results.html', {'score': score, 'total': total})
def questions_page(request):
    return render(request, 'quizes/questions.html')
def home_page(request):
    if request.method == 'POST':
        quiz_name = request.POST.get('quiz_name')
        quiz = Quiz.objects.filter(name=quiz_name).first()
        time_in_seconds = quiz.time * 60
        return render(request, 'quizes/questions.html', {'quiz': quiz, 'time_in_seconds': time_in_seconds})
    quizes = Quiz.objects.all()
    return render(request, 'quizes/home.html', {'quizes': quizes})
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful, you can take your quiz!')
            return redirect('home-view')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'quizes/login.html')

def logout_page(request): 
    logout(request)
    return render(request, 'quizes/home.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'quizes/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'quizes/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'registration/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        if user:
            return redirect('login-view')
        else:
            messages.error(request, 'Registration failed, try again!')
    return render(request, 'quizes/register.html')

def search_page(request):
    quiz = Quiz.objects.filter(name='Land Laws')
    return render(request, 'quizes/search.html', {'quiz': quiz})