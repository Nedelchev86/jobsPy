
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsPy.main.urls')),
    path('accounts/', include('jobsPy.accounts.urls')),
    path('jobseeker/', include('jobsPy.jobseekers.urls')),
]
