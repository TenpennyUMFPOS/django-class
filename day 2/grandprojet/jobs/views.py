from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import JobRecord, Contract, Skill, Industry, Candidate
from .serializers import (
    JobRecordSerializer,
    ContractSerializer,
    SkillSerializer,
    IndustrySerializer,
    CandidateSerializer
)

class JobRecordViewSet(viewsets.ModelViewSet):
    queryset = JobRecord.objects.all()
    serializer_class = JobRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
