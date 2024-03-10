from django.urls import path
from jobsPy.accounts.views import RedirectDashboardView
from jobsPy.company.views import AllCompany
from jobsPy.main.views import IndexView, JobsCategory

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', RedirectDashboardView.as_view(), name="login_redirect_dashboard"),
    path('category/<slug:category_slug>/', JobsCategory.as_view(), name='jobs_category'),
    path('company_lsit/', AllCompany.as_view(), name="all_company"),

]
