from django.urls import path

from jobsPy.jobseekers.views import JobSeekerDashboard, EditProfile, FavouriteJobs, ApplyJobs

urlpatterns = [
    path("dashboard/", JobSeekerDashboard.as_view(), name="job seeker dashboard"),
    path("edit-profile/<int:pk>/", EditProfile.as_view(), name="edit-profile"),
    # path("edit-profile/", EditProfile.as_view(), name="edit-profile"),
    path("favourite-jobs/", FavouriteJobs.as_view(), name="favourite_jobs"),
    path("apply-jobs/", ApplyJobs.as_view(), name="jobs-apply"),
]