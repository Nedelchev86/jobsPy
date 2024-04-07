
from django.contrib import admin
from .models import Job, Category, Applicant, Skills


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'deadline', 'is_published')
    list_filter = ('category', 'location', 'deadline', 'is_published')
    search_fields = ('title', 'description', 'responsibilities', 'location', 'salary')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ["user"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'created_at', 'get_status', 'comment')
    list_filter = ('job__title', 'created_at', 'status')
    search_fields = ('user__username', 'job__title', 'comment')

    def get_status(self, obj):
        return obj.get_status
    get_status.short_description = 'Status'


@admin.register(Skills)
class AdminJSkills(admin.ModelAdmin):
    pass
