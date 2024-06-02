from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(f'CAT: {self.quiz.name}, Username: {self.user.username}, Score: {self.score}')
