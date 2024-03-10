from django.contrib import admin

from jobsPy.jobs.models import Job, Category, Skills


# Register your models here.
@admin.register(Job)
class AdminJobs(admin.ModelAdmin):
    pass

@admin.register(Category)
class AdminJCategory(admin.ModelAdmin):
    pass


@admin.register(Skills)
class AdminJSkills(admin.ModelAdmin):
    pass