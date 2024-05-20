from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Company, Statistics, OfficeHours, SocialNetworks, Partners, Steps, StepDetails, Blogs, FAQ, FAQInfo
from .serializers import (
    CompanySerializer, StatisticsSerializer, OfficeHoursSerializer, SocialNetworksSerializer, PartnersSerializer,
    StepsSerializer, StepDetailsSerializer, BlogsSerializer, FAQSerializer, FAQInfoSerializer
)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class OfficeHoursViewSet(viewsets.ModelViewSet):
    queryset = OfficeHours.objects.all()
    serializer_class = OfficeHoursSerializer

class SocialNetworksViewSet(viewsets.ModelViewSet):
    queryset = SocialNetworks.objects.all()
    serializer_class = SocialNetworksSerializer

class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class StepsViewSet(viewsets.ModelViewSet):
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer

class StepDetailsViewSet(viewsets.ModelViewSet):
    queryset = StepDetails.objects.all()
    serializer_class = StepDetailsSerializer

class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQInfoViewSet(viewsets.ModelViewSet):
    queryset = FAQInfo.objects.all()
    serializer_class = FAQInfoSerializer
