from django.contrib import admin

from jobsPy.jobseekers.models import JobSeeker


# Register your models here.
@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    pass


