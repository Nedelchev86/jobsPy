from django.contrib import auth
from django.contrib.auth import get_user_model, login, alogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from jobsPy.accounts.forms import RegisterUserForm, LoginForm, ChangePassword

userMode = get_user_model()

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm

    # Static way of providing `success_url`
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


@login_required(login_url='login')
def singout(request):
    auth.logout(request)
     # messages.success(request, 'You are logged out.')
    return redirect('index')

# def singout(request):
#     alogout(request)
    # Redirect to a success page.
# class singout(LogoutView):
#     template_name = "logout.html"
#
#

class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm

    # def get_success_url(self):
    #     if self.request.user.role == "jobseeker":
    #         return reverse_lazy("index")
    #     return super().get_success_url()



class ChangePass(PasswordChangeView):
    form_class = ChangePassword

    template_name = "accounts/chage_password.html"
    success_url = reverse_lazy('login_redirect_dashboard')
