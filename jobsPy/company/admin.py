from django.contrib import admin

from jobsPy.company.models import CompanyProfile


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('user' ,'name', 'location', 'email', 'get_all_applicant', 'activated')
    list_filter = ('activated', 'location')
    search_fields = ('name', 'location', 'email')

    def get_all_applicant(self, obj):
        return obj.get_all_applicant
    get_all_applicant.short_description = 'Total Applicants'