import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from .forms import FeedbackForm
from jobs.models import JobRecord
from django.db.models import Avg
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def list_feedback(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    feedbacks = Feedback.objects.filter(job=job).values('id', 'content', 'rating', 'created_at')  # example fields
    moyenne = feedbacks.aggregate_avg = feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0

    feedback_list = list(feedbacks)  # QuerySet -> list of dicts

    return JsonResponse({
        'feedbacks': feedback_list,
        'average_rating': round(moyenne, 2),
    })

@csrf_exempt  # only if you want to skip CSRF for testing, otherwise handle token properly
@require_http_methods(["POST"])
def add_feedback(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)

    try:
        data = json.loads(request.body)
        content = data.get('content')
        rating = data.get('rating')
        if not content or not rating:
            return HttpResponseBadRequest("Missing content or rating")
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    feedback = Feedback.objects.create(job=job, content=content, rating=rating)
    return JsonResponse({
        'id': feedback.id,
        'content': feedback.content,
        'rating': feedback.rating,
        'created_at': feedback.created_at,
    })