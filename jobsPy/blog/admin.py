from django.contrib import admin

from jobsPy.blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
