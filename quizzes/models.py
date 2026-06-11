from django.db import models
from learning.models import Subject, Topic


class Question(models.Model):

    LEVEL_CHOICES = [
        ("basic", "Basic"),
        ("moderate", "Moderate"),
        ("difficult", "Difficult"),
    ]

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES
    )

    question_text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]