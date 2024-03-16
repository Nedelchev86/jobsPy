from django.contrib.auth import get_user_model
from django.db import models

from jobsPy.jobs.models import Applicant, Skills

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
    nationality = models.CharField(max_length=50, blank=False, null=False)
    occupation = models.CharField(max_length=50, blank=False, null=False)
    website = models.CharField(max_length=70, blank=True, null=True)
    linkedin = models.CharField(blank=False, null=False, max_length=50)
    github = models.CharField(blank=False, null=False, max_length=50)
    about = models.TextField()
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(
        blank=True, null=True, upload_to='images/profile')
    gender = models.CharField(blank=False, null=False,
                              choices=GENDER_TYPE, max_length=1)
    marital_status = models.CharField(blank=False, null=False, max_length=20, choices=MARITAL_STATUS)
    skills = models.ManyToManyField(Skills, related_name="skills")


    @property
    def get_user_all_applicant(self):
        return Applicant.objects.filter(user=self.user).count()


class Education(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)