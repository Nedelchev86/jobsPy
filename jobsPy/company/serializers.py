from rest_framework import serializers
from .models import CompanyProfile
from ..jobs.models import Skills


class CompanyProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Skills.objects.all())
    class Meta:
        model = CompanyProfile
        fields = '__all__'  # or specify fields explicitly