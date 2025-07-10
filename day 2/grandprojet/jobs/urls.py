from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    JobRecordViewSet,
    ContractViewSet,
    SkillViewSet,
    IndustryViewSet,
    CandidateViewSet
)

router = DefaultRouter()
router.register(r'jobs', JobRecordViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'industries', IndustryViewSet)
router.register(r'candidates', CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
