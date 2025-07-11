from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.paginator import Paginator

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

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['job_title', 'employee_residence']
    ordering_fields = ['salary_in_usd', 'created_at']

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

def jobrecord_list(request):

    jobrecords = JobRecord.objects.all().order_by('-id')
    

    paginator = Paginator(jobrecords, 10)

    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

  
    return render(request, 'jobrecord_list.html', {'page_obj': page_obj})