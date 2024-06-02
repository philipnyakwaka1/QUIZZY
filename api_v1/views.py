from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from quizes.models import Quiz
from results.models import Result
from .serializers import QuizSerializer, ResultSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view

@api_view(['POST'])
def submit_page(request):
    if request.method == 'POST':
        score = request.data.get('score')
        quiz_name = request.data.get('quiz_name')
        quiz = Quiz.objects.filter(name=quiz_name).first()
        user = request.user
        if Result.objects.filter(user=user, quiz=quiz).exists():
            return Response({'detail': 'You have already taken this test, You cannot retake!'}, status=status.HTTP_400_BAD_REQUEST)
        result = Result.objects.create(
            quiz=quiz,
            user=user,
            score=score,
        )
        serializer = ResultSerializer(result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        results = Result.objects.all()
        courses = Quiz.objects.all()
        serializer = ProfileSerializer({'results': results, 'courses': courses, 'today': date.today()})
        return Response(serializer.data)

class ResultsViewSet(viewsets.ViewSet):
    def list(self, request):
        score = request.query_params.get('score')
        total = request.query_params.get('total')
        if score is None or total is None:
            return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            score = int(score)
            total = int(total)
        except ValueError:
            return Response({"detail": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'score': score, 'total': total})

class QuizViewSet(viewsets.ViewSet):
    def list(self, request):
        quizes = Quiz.objects.all()
        serializer = QuizSerializer(quizes, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def login_page(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'detail': 'Login successful, you can take your quiz!'})
        else:
            return Response({'detail': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_page(request):
    logout(request)
    return Response({'detail': 'Logged out successfully'})

@api_view(['POST'])
def register_page(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if password != confirm_password:
            return Response({'detail': 'Passwords do not match!'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'detail': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'detail': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, email=email, password=password)
        if user:
            return Response({'detail': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Registration failed, try again!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_page(request):
    quiz = Quiz.objects.filter(name='Land Laws')
    serializer = QuizSerializer(quiz, many=True)
    return Response(serializer.data)
