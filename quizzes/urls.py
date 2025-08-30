from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_list, name="quiz_list"),
    path("<int:pk>/", views.quiz_detail, name="quiz_detail"),
    path("<int:pk>/take/", views.take_quiz, name="take_quiz"),
    path("<int:pk>/submit/", views.submit_quiz, name="submit_quiz"),
    path("submission/<int:pk>/", views.view_submission, name="view_submission"),
    path("submission/<int:pk>/progress/", views.submission_progress, name="submission_progress"),
]

