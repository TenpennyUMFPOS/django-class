from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    JobRecordViewSet,
    ContractViewSet,
    SkillViewSet,
    IndustryViewSet,
    CandidateViewSet,
    jobrecord_list
)


router = DefaultRouter()
router.register(r'jobs', JobRecordViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'industries', IndustryViewSet)
router.register(r'candidates', CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jobrecords/', jobrecord_list, name='jobrecord_list'),
    
]
