import json

from rest_framework import serializers
from .models import Job, Skills, Applicant
from ..company.models import CompanyProfile


class JobSerializer(serializers.ModelSerializer):
    needed_skills = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Skills.objects.all())
    class Meta:
        model = Job
        fields = '__all__'


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'  # Include additional fields as needed


class JobsDetailSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    needed_skills = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Skills.objects.all())

    class Meta:
        model = Job
        fields = '__all__'
    def get_company(self, obj):
        user_id = obj.user_id


        try:
            user = CompanyProfile.objects.get(pk=user_id)

            return user.name
        except CompanyProfile.DoesNotExist:
            return None


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'