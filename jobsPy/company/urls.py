from django.urls import path
from jobsPy.company.views import CompanyDashboard, CreatedJobs, EditCompany, CompanyApplicant, ApplicantList, \
    CompanyDetails, AllCompany, CompanyDeleteView, CompanyDeletedView
from jobsPy.jobs.views import ChangeStatus

urlpatterns = [
    path('dashboard/', CompanyDashboard.as_view(), name="company-dashboard"),
    path('created-jobs/', CreatedJobs.as_view(), name="created-jobs"),
    path('edit-company/<int:pk>/', EditCompany.as_view(), name="edit-company-profile"),
    path('company-applicant/', CompanyApplicant.as_view(), name="jobs-applicants"),
    path('company-applicant/jobs-aplicant/<int:pk>/', ApplicantList.as_view(), name="applicant_list"),
    path('change-status/<int:pk>/', ChangeStatus.as_view(), name="change-status"),
    path('details/<int:pk>/', CompanyDetails.as_view(), name="company-details"),
    path('', AllCompany.as_view(), name="all_company"),
    path('delete/', CompanyDeleteView.as_view(), name='delete_company'),
    path('deleted/', CompanyDeletedView.as_view(), name='deleted_success_company'),

]
