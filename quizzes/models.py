from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time_limit_seconds = models.PositiveIntegerField(default=0, help_text="0 = no limit")
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class Question(models.Model):
    SINGLE = "S"
    MULTI = "M"
    QUESTION_TYPES = [(SINGLE, "Single Choice"), (MULTI, "Multiple Choice")]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    type = models.CharField(max_length=1, choices=QUESTION_TYPES, default=SINGLE)
    points = models.PositiveIntegerField(default=1)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Q{self.order}: {self.text[:50]}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="submissions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    started_at = models.DateTimeField(default=timezone.now)
    submitted_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    @property
    def is_submitted(self):
        return self.submitted_at is not None

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(Choice)   # ✅ multiple choices


