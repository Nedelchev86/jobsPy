from django.urls import path

from jobsPy.accounts.views import RedirectDashboardView
from jobsPy.main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', RedirectDashboardView.as_view(), name="login_redirect_dashboard"),

]
