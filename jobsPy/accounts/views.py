from django.contrib import auth
from django.contrib.auth import get_user_model, login, alogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.forms import EmailInput
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View

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

    template_name = "chage_password.html"
    success_url = reverse_lazy('login_redirect_dashboard')


class RedirectDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_type = request.user.role

        if user_type == 'company':
            return redirect('company-dashboard')
        elif user_type == 'jobseeker':
            return redirect('job seeker dashboard')
        else:
            # Handle other roles or situations
            return redirect('index')  # Redirect to a default page if the role is not recognized
