from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from .forms import FeedbackForm
from jobs.models import JobRecord
from django.db.models import Avg

def list_feedback(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    feedbacks = Feedback.objects.filter(job=job)
    moyenne = feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0
    return render(request, 'feedback/list_feedback.html', {
        'job': job,
        'feedbacks': feedbacks,
        'moyenne': round(moyenne, 2),
    })

def add_feedback(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.job = job
            feedback.save()
            return redirect('feedback_list', job_id=job.id)
    else:
        form = FeedbackForm()
    return render(request, 'feedback/add_feedback.html', {'form': form, 'job': job})
