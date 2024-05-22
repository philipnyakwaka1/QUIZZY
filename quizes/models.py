from django.db import models

DIFF_CHOICES = (("easy", "easy"), ("medium", "medium"), ("hard", "hard"))
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="Required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self) -> str:
        return f"{self.name} - {self.topic}"
    
    def get_questions(self):
        return self.questions.all()

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"