from django.urls import path

from jobsPy.jobseekers.views import JobSeekerDashboard, EditProfile, FavouriteJobs, ApplyJobs, JobSeekerDetails, \
    AllEmployees, AddEducation, AddWorkExperience, EditEducation, EditWorkExperience, JobSeekerDeleteView, \
    ProfileDeletedView, DeleteEducation, DeleteWorkExperience, JobSeekerNotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path("all/", AllEmployees.as_view(), name="all-employees"),
    path("dashboard/", JobSeekerDashboard.as_view(), name="job seeker dashboard"),
    # path("edit-profile/<int:pk>/", EditProfile.as_view(), name="edit-profile"),
    path("edit-profile/", EditProfile.as_view(), name="edit-profile"),
    path("details/<int:pk>/", JobSeekerDetails.as_view(), name="jobseeker details"),
    path("add-education/<int:pk>/", AddEducation.as_view(), name="add-education"),
    path("edit-education/<int:pk>/", EditEducation.as_view(), name="edit-education"),
    path("add-work-experience/<int:pk>/", AddWorkExperience.as_view(), name="add-work-experience"),
    path("edit-work-experience/<int:pk>/", EditWorkExperience.as_view(), name="edit-work-experience"),
    path("favourite-jobs/", FavouriteJobs.as_view(), name="favourite_jobs"),
    path("apply-jobs/", ApplyJobs.as_view(), name="jobs-apply"),
    path('delete/', JobSeekerDeleteView.as_view(), name='delete_profile'),
    path('deleted/', ProfileDeletedView.as_view(), name='deleted_success'),
    path('delete-education/<int:pk>', DeleteEducation.as_view(), name='delete education'),
    path('delete-experience/<int:pk>', DeleteWorkExperience.as_view(), name='delete work experience'),
    path('notifications/', JobSeekerNotificationListView.as_view(), name='job seeker notifications'),
    path('notifications/<int:pk>/mark_as_read/', MarkNotificationAsReadView.as_view(), name='mark_as_read_job_seeker'),

]
