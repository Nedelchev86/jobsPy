from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from jobsPy.jobs.models import Applicant, Skills

UserModel = get_user_model()


class CompanyProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True, related_name="company")
    name = models.CharField(max_length=40, null=False, blank=False)
    description = RichTextField(null=False, blank=False)
    location = models.CharField(max_length=40, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(max_length=254, null=False, blank=False)
    image = CloudinaryField('image', blank=True, null=True)
    website_url = models.URLField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)
    facebook_url = models.URLField(max_length=200, null=True, blank=True)
    employees = models.PositiveIntegerField(null=False, blank=False, default=0)
    foundation_year = models.PositiveIntegerField(null=False, blank=False, default=0)
    skills = models.ManyToManyField(Skills, related_name="technologies", verbose_name="Technologies")
    activated = models.BooleanField(default=False)

    def __str__(self):
        if self.name:
            return self.name
        return str(self.user)

    @property
    def get_all_applicant(self):

        return Applicant.objects.filter(job__user=self.user, job__is_published=True).count()

    class Meta:
        ordering = ['-pk']
