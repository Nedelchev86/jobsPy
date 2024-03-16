from django.urls import path

from jobsPy.jobseekers.views import JobSeekerDashboard, EditProfile, FavouriteJobs, ApplyJobs, JobSeekerDetails, \
    AllEmployees, AddEducation

urlpatterns = [
    path("all/", AllEmployees.as_view(), name="all-employees"),
    path("dashboard/", JobSeekerDashboard.as_view(), name="job seeker dashboard"),
    path("edit-profile/<int:pk>/", EditProfile.as_view(), name="edit-profile"),
    path("details/<int:pk>/", JobSeekerDetails.as_view(), name="job seeker-details"),
    path("add-education/<int:pk>/", AddEducation.as_view(), name="add-education"),
    # path("edit-profile/", EditProfile.as_view(), name="edit-profile"),
    path("favourite-jobs/", FavouriteJobs.as_view(), name="favourite_jobs"),
    path("apply-jobs/", ApplyJobs.as_view(), name="jobs-apply"),
]