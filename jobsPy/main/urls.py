from django.urls import path
from jobsPy.accounts.views import RedirectDashboardView
from jobsPy.main.views import IndexView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('dashboard/', RedirectDashboardView.as_view(), name="login_redirect_dashboard"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)