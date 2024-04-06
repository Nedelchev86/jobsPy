from django.urls import path

from jobsPy.accounts.forms import CustomPasswordResetForm
from jobsPy.accounts.views import RegisterView, ChangePass, LoginUserView, singout, select_role
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("registration/", RegisterView.as_view(), name="registration"),
    path('login/', LoginUserView.as_view(), name="login"),
    path("logout/", singout, name="sing-out"),
    path("chage-password/", ChangePass.as_view(), name="change-password"),
    path('select-role/', select_role, name='select_role'),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
