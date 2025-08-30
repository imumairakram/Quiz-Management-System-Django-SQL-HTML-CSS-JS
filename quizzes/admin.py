from django.contrib import admin
from .models import Quiz, Question, Choice, Submission, Answer
from quizzes import models


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_by", "created_at")
    list_filter = ("is_published",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("quiz", "order", "type", "points")
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "text", "is_correct")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("quiz", "user", "score", "submitted_at")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("submission", "question")
