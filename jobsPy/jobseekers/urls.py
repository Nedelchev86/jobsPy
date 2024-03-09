from django.urls import path

from jobsPy.jobseekers.views import JobSeekerDashboard, EditProfile

urlpatterns = [
    path("dashboard/", JobSeekerDashboard.as_view(), name="job seeker dashboard"),
    path("edit-profile/<int:pk>/", EditProfile.as_view(), name="edit-profile"),
]