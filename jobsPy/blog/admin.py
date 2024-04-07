from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views')
    search_fields = ['title', 'author__user__email']
    list_filter = ('created_at',)
    readonly_fields = ('views', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', "views")
        }),
        ('Content', {
            'fields': ('description', 'more_info')
        }),
        ('Images', {
            'fields': ('image_url_1', 'image_url_2', 'image_url_3')
        }),

    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'created_at')
    search_fields = ['content', 'author__email', 'post__title']
    readonly_fields = ["author"]
    list_filter = ('created_at',)
