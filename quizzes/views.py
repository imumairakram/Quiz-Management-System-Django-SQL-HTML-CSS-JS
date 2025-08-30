from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Quiz, Question, Choice, Submission, Answer

def quiz_list(request):
    quizzes = Quiz.objects.filter(is_published=True).select_related()
    return render(request, "quizzes/quiz_list.html", {"quizzes": quizzes})

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, is_published=True)
    return render(request, "quizzes/quiz_detail.html", {"quiz": quiz})

@login_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, is_published=True)
    submission, _ = Submission.objects.get_or_create(
        quiz=quiz, user=request.user, submitted_at__isnull=True, defaults={}
    )
    questions = quiz.questions.prefetch_related("choices")
    return render(request, "quizzes/quiz_take.html", {
        "quiz": quiz, "submission": submission, "questions": questions
    })

def submit_quiz(request, pk):
    if request.method != "POST":
        raise Http404()

    quiz = get_object_or_404(Quiz, pk=pk, is_published=True)

    submission, _ = Submission.objects.get_or_create(
        quiz=quiz, user=request.user, submitted_at__isnull=True
    )

    total = 0
    score = 0
    for q in quiz.questions.all():
        total += q.points
        selected = request.POST.getlist(f"question_{q.id}")
        # save answers
        answer, _ = Answer.objects.get_or_create(
            submission=submission, question=q
        )
        answer.selected_choices.set(selected)

        correct_ids = set(str(c.id) for c in q.choices.filter(is_correct=True))
        if set(selected) == correct_ids:
            score += q.points

    submission.max_score = total
    submission.score = score
    submission.submitted_at = timezone.now()
    submission.save()

    return JsonResponse({"ok": True, "submission_id": submission.id})

@login_required
def view_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk, user=request.user)
    quiz = submission.quiz
    qa = []
    for q in quiz.questions.prefetch_related("choices"):
        ans = submission.answers.filter(question=q).first()
        picked = set(int(i) for i in ans.selected_choice_ids.split(",") if ans and ans.selected_choice_ids and i.isdigit())
        qa.append({
            "question": q,
            "choices": q.choices.all(),
            "selected_ids": picked,
            "correct_ids": set(c.id for c in q.choices.filter(is_correct=True)),
        })
    return render(request, "quizzes/results.html", {"submission": submission, "qa": qa})

@login_required
def submission_progress(request, pk):
    submission = get_object_or_404(Submission, pk=pk, user=request.user)
    answered = submission.answers.count()
    total = submission.quiz.questions.count()
    return JsonResponse({
        "answered": answered,
        "total": total,
        "progress_pct": round(100 * answered / max(total, 1), 2),
    })

