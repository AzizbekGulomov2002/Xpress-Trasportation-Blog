from rest_framework import serializers
from .models import Company, Statistics, OfficeHours, SocialNetworks, Partners, Steps, StepDetails, Blogs, FAQ, FAQInfo

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'

class OfficeHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHours
        fields = '__all__'

class SocialNetworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworks
        fields = '__all__'

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = '__all__'

class StepDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepDetails
        fields = '__all__'

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQInfo
        fields = '__all__'
