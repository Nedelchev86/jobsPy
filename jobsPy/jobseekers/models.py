from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

from jobsPy.jobs.models import Applicant, Skills
from jobsPy.main.models import Seniority

UserModel = get_user_model()

GENDER_TYPE = (
    ('M', "Male"),
    ('F', "Female"),
)
MARITAL_STATUS= (
     ('Married', "Married"),
    ('Unmarried', "Unmarried"),
    ('Devorced', "Devorced"),
)


class JobSeeker(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    nationality = models.CharField(max_length=50, blank=False, null=False)
    occupation = models.CharField(max_length=50, blank=False, null=False)
    seniority = models.ForeignKey(Seniority, on_delete=models.SET_NULL, blank=True, null=True)
    website = models.URLField(max_length=70, blank=True, null=True)
    linkedin = models.URLField(blank=False, null=False, max_length=50)
    github = models.URLField(blank=False, null=False, max_length=50)
    about = RichTextField(blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(
        blank=True, null=True, upload_to='images/profile')
    gender = models.CharField(blank=False, null=False,
                              choices=GENDER_TYPE, max_length=1)
    marital_status = models.CharField(blank=False, null=False, max_length=20, choices=MARITAL_STATUS)
    skills = models.ManyToManyField(Skills, related_name="skills")
    activated = models.BooleanField(default=False)

    @property
    def get_user_all_applicant(self):
        return Applicant.objects.filter(user=self.user).count()


class Education(models.Model):

    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='educations')
    image = models.URLField(max_length=200, blank=True, null=True)
    institution = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Experience(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='experience')
    image = models.URLField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
