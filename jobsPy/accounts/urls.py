from django.urls import path

from jobsPy.accounts.views import RegisterView, singout, ChangePass, LoginUserView

urlpatterns = [
    path("registration/", RegisterView.as_view(), name="registration"),
    path('login/', LoginUserView.as_view(), name="login"),
    path("sing-out/", singout, name="sing-out"),
    path("chage-password/", ChangePass.as_view(), name="change-password"),
    path('login/', LoginUserView.as_view(), name="login"),

]
