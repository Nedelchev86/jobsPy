from rest_framework import serializers
from .models import Job, Skills


class JobSerializer(serializers.ModelSerializer):
    needed_skills = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Skills.objects.all())
    class Meta:
        model = Job
        fields = '__all__'