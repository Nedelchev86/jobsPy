from django.contrib.auth import get_user_model
from rest_framework import serializers

from jobsPy.blog.models import BlogPost, Comment
from jobsPy.company.models import CompanyProfile
from jobsPy.jobseekers.models import JobSeeker
userModel = get_user_model()

class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['first_name', 'last_name', 'user']
        # read_only_fields = ['first_name', 'last_name', 'pk']




class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
    def get_author(self, obj):
        # Check if the author is a jobseeker
        user = obj.author
        if user.role == 'jobseeker':
            jobseeker = user.jobseeker
            return CommentJobSeekerSerializer(jobseeker).data
        else:
            company = user.company
            return CommentCompanySerializer(company).data



class CommentJobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['first_name', 'last_name', 'profile_picture', 'pk']


        # read_only_fields = ['first_name', 'last_name', 'pk']

class CommentCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['title', 'image', 'pk']


class CommentSerializerCreate(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['content', 'author']
    def get_author(self, obj):
        # Check if the author is a jobseeker
        user = obj.author
        if user.role == 'jobseeker':
            jobseeker = user.jobseeker
            return CommentJobSeekerSerializer(jobseeker).data
        else:
            company = user.company
            return CommentCompanySerializer(company).data


class BlogPostSerializer(serializers.ModelSerializer):
    author = JobSeekerSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'





