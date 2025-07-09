from django.urls import path
from . import views

urlpatterns = [
    path('<int:job_id>/', views.list_feedback, name='feedback_list'),
    path('add/<int:job_id>/', views.add_feedback, name='add_feedback'),
]
