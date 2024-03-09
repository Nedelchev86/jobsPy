from django.urls import path

from jobsPy.accounts.views import RegisterView, ChangePass, LoginUserView, singout

urlpatterns = [
    path("registration/", RegisterView.as_view(), name="registration"),
    path('login/', LoginUserView.as_view(), name="login"),
    path("logout/", singout, name="sing-out"),
    path("chage-password/", ChangePass.as_view(), name="change-password"),


]
