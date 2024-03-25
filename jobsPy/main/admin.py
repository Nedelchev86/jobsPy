from django.contrib import admin

from jobsPy.main.models import Seniority


# Register your models here.
@admin.register(Seniority)
class SeniorityAdmin(admin.ModelAdmin):
    pass