from django.contrib import admin
from .models import Seniority, Contact, Subscriber

@admin.register(Seniority)
class SeniorityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone', 'created_on', 'processed')
    list_filter = ('processed',)
    search_fields = ('name', 'subject', 'email')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email',)
