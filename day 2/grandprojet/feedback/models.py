from django.db import models
from jobs.models import JobRecord

class Feedback(models.Model):
    job = models.ForeignKey(JobRecord, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.job.job_title} - {self.rating}★"
