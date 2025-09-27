from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Option, Submission
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    quizzes = Quiz.objects.all()  # you can filter by active/published
    return render(request, 'quizzes/dashboard.html', {'quizzes': quizzes})


@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})


@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = 0
    total = quiz.questions.count()

    for question in quiz.questions.all():
        selected_option = request.POST.get(str(question.id))
        if selected_option:
            option = Option.objects.get(id=selected_option)
            if option.is_correct:
                score += 1

    Submission.objects.create(student=request.user, quiz=quiz, score=score)
    percentage = (score / total) * 100 if total > 0 else 0
    return render(request, 'quizzes/result.html', {'quiz': quiz, 'score': score, 'total': total, 'percentage': percentage})
