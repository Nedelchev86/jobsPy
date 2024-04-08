from django.urls import path
from jobsPy.accounts.views import RedirectDashboardView
from jobsPy.main.views import IndexView, SubscribeToNewsletterView, SubscribeSuccessView, MailSuccessView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', RedirectDashboardView.as_view(), name="login_redirect_dashboard"),
    path('subscribe/', SubscribeToNewsletterView.as_view(), name='subscribe'),
    path('subscribe-success/', SubscribeSuccessView.as_view(), name='subscribe success'),
    path('mail-success/', MailSuccessView.as_view(), name='mail success'),

]
