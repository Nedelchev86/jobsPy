
from django.contrib import admin
from django.urls import path, include
from jobsPy.main.views import Contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsPy.main.urls')),
    path('accounts/', include('jobsPy.accounts.urls')),
    path('jobseeker/', include('jobsPy.jobseekers.urls')),
    path('company/', include('jobsPy.company.urls')),
    path('jobs/', include('jobsPy.jobs.urls')),
    path('contact/', Contact.as_view(), name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)