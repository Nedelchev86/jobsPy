
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from jobsPy.main.views import Contact, ContactFrom, NewsletterCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsPy.main.urls')),
    path('accounts/', include('jobsPy.accounts.urls')),
    path('jobseeker/', include('jobsPy.jobseekers.urls')),
    path('company/', include('jobsPy.company.urls')),
    path('jobs/', include('jobsPy.jobs.urls')),
    path('contact/', ContactFrom.as_view(), name="contact"),
    path('newsletter/', NewsletterCreateView.as_view(), name="newsletter"),
    path('api2/', include('jobsPy.blog.api.urls')),
    path('blog/', include('jobsPy.blog.urls')),
    path('notifications/', include('jobsPy.notifications.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('jobsPy.api.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)

handler403 = 'jobsPy.main.views.custom_403'


