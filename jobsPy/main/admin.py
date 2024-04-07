from django.contrib import admin

from jobsPy.main.models import Seniority, Contact, Subscriber


# Register your models here.
@admin.register(Seniority)
class SeniorityAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass
