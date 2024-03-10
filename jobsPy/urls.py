
from django.contrib import admin
from django.urls import path, include

from jobsPy.main.views import Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsPy.main.urls')),
    path('accounts/', include('jobsPy.accounts.urls')),
    path('jobseeker/', include('jobsPy.jobseekers.urls')),
    path('company/', include('jobsPy.company.urls')),
    path('jobs/', include('jobsPy.jobs.urls')),
    path('contact/', Contact.as_view(), name="contact"),
]
