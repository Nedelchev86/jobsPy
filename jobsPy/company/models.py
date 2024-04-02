from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

from jobsPy.jobs.models import Applicant

UserModel = get_user_model()

class CompanyProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True, related_name="company")
    name = models.CharField(max_length=40, null=False, blank=False)
    description = RichTextField(null=False, blank=False)
    location = models.CharField(max_length=40, null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(max_length=254, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="company/image")
    website_url = models.URLField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)
    facebook_url = models.URLField(max_length=200, null=True, blank=True)
    employees = models.PositiveIntegerField(null=False, blank=False)
    year_of_foundation = models.PositiveIntegerField(null=False, blank=False)
    activated = models.BooleanField(default=False)


    @property
    def get_all_applicant(self):

        return Applicant.objects.filter(job__user=self.user, job__is_published=True).count()