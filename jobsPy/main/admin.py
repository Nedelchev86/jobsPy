from django.contrib import admin
from .models import Seniority, Contact, Subscriber, Newsletter


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


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
