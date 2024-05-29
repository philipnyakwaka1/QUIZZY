from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from questions.models import Question, Answer
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Quiz
from results.models import Result
from django.contrib.auth.decorators import login_required

def questions_page(request):
    return render(request, 'quizes/questions.html')
def home_page(request):
    quiz_name = request.POST.get('quiz_name')
    quiz = Quiz.objects.filter(name=quiz_name).first()
    return render(request, 'quizes/questions.html', {'quiz': quiz})

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
    return render(request, 'quizes/base.html')

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