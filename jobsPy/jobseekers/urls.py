from django.urls import path

from jobsPy.jobseekers.views import JobSeekerDashboard

urlpatterns = [
    path("dashboard/", JobSeekerDashboard.as_view(), name="job seeker dashboard"),
]