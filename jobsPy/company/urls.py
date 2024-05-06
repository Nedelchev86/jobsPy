from django.urls import path, include
from rest_framework.routers import DefaultRouter

from jobsPy.company.views import CompanyDashboard, CreatedJobs, EditCompany, CompanyApplicant, ApplicantList, \
    CompanyDetails, AllCompany, CompanyDeleteView, CompanyDeletedView, CompanyProfileViewSet
from jobsPy.jobs.views import ChangeStatus, subscribe_to_company
from jobsPy.notifications.views import CompanyNotificationListView, MarkCompanyNotificationAsReadView


router = DefaultRouter()
router.register(r'api/companies', CompanyProfileViewSet)

urlpatterns = [
    path('dashboard/', CompanyDashboard.as_view(), name="company-dashboard"),
    path('created-jobs/', CreatedJobs.as_view(), name="created-jobs"),
    path('edit-company/', EditCompany.as_view(), name="edit-company-profile"),
    path('company-applicant/', CompanyApplicant.as_view(), name="jobs-applicants"),
    path('company-applicant/jobs-aplicant/<int:pk>/', ApplicantList.as_view(), name="applicant_list"),
    path('change-status/<int:pk>/', ChangeStatus.as_view(), name="change-status"),
    path('details/<int:pk>/', CompanyDetails.as_view(), name="company-details"),
    path('notifications/', CompanyNotificationListView.as_view(), name="company-notifications"),
    path('notifications/<int:pk>/mark_as_read/', MarkCompanyNotificationAsReadView.as_view(), name='mark_as_read_company'),
    path('', AllCompany.as_view(), name="all_company"),
    path('delete/', CompanyDeleteView.as_view(), name='delete_company'),
    path('deleted/', CompanyDeletedView.as_view(), name='deleted_success_company'),
    path('details/<int:pk>/subscribe/', subscribe_to_company, name='subscribe_to_company'),
    # path('api/companies/', CompanyProfileViewSet.as_view(), name="company api"),
    path('', include(router.urls)),

]
