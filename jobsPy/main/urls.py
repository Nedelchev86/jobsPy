from django.urls import path
from jobsPy.accounts.views import RedirectDashboardView
from jobsPy.company.views import AllCompany
from jobsPy.main.views import IndexView, JobsCategory


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', RedirectDashboardView.as_view(), name="login_redirect_dashboard"),

]


