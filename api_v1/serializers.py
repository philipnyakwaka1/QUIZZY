# api_v1/serializers.py

from rest_framework import serializers
from quizes.models import Quiz
from results.models import Result

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
