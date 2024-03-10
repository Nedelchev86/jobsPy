from django.contrib import admin

from jobsPy.company.models import CompanyProfile


# Register your models here.

@admin.register(CompanyProfile)
class CompanyAdmin(admin.ModelAdmin):

    search_fields = ['name', 'email']

