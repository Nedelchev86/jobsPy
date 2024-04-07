from django.urls import path
from jobsPy.accounts.views import RedirectDashboardView
from jobsPy.company.views import AllCompany
from jobsPy.main.views import IndexView, JobsCategory, SubscribeToNewsletterView, SubscribeSuccessView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', RedirectDashboardView.as_view(), name="login_redirect_dashboard"),
    path('subscribe/', SubscribeToNewsletterView.as_view(), name='subscribe'),
    path('subscribe-success/', SubscribeSuccessView.as_view(), name='subscribe success'),

]


