from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from jobsPy.main.models import Seniority

# Create your models here.

UserModel = get_user_model()


class Skills(models.Model):
    name = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.name


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=5)
    return unique_slug


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)


JOB_TYPE = (
    ('fulltime', "Full time"),
    ('parttime', "Part time"),
    ('remote', "Remote"),
    ('internship', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(UserModel,  on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    seniority = models.ForeignKey(Seniority, on_delete=models.SET_NULL, blank=True, null=True)
    description = RichTextField(null=False, blank=False)
    responsibilities = RichTextField(null=False, blank=False)
    benefits = RichTextField(null=True, blank=True)
    # job_image = models.ImageField(null=True, blank=True, upload_to="jobs/image", default="images/default/default.jpg")
    job_image = CloudinaryField('image', blank=True, null=True)
    vacancy = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=300,)
    job_type = models.CharField(choices=JOB_TYPE, max_length=10)
    salary = models.CharField(max_length=30, blank=True)
    deadline = models.DateField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    needed_skills = models.ManyToManyField(Skills, related_name="needed_skills")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class FavoriteJob(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')  # Ensure a job can be favorited only once per user


class Applicant(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ["id"]
        unique_together = ["user", "job"]

    @property
    def get_status(self):
        if self.status == 1:
            return "Pending"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"

