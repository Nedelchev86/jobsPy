from django.urls import path


from jobsPy.jobs.views import JobCreateView, JobDetails, EditJob, AllJobsView, \
    RemoveFromFavoritesView, add_to_favorites, apply_for_job
from jobsPy.jobseekers.views import FavouriteJobs, ApplyJobs

urlpatterns = [
    path('create-job/', JobCreateView.as_view(), name="create_job"),
    path('edit-job/<int:pk>/', EditJob.as_view(), name="edit_job"),
    path("job-details/<int:pk>/", JobDetails.as_view(), name="job_details"),
    path("all/", AllJobsView.as_view(), name="all-jobs"),
    path("add-to-favourite/<int:pk>/", add_to_favorites, name="add-to-favourite"),
    path("remove-from-favourite/<int:pk>/", RemoveFromFavoritesView.as_view(), name="remove_From_fav"),
    path("apply_for_job/<int:pk>/", apply_for_job, name="apply_for_job"),
    path("favourite-jobs/", FavouriteJobs.as_view(), name="favourite_jobs"),
    path("apply-jobs/", ApplyJobs.as_view(), name="jobs-apply"),

]
