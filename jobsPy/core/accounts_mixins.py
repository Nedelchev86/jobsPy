from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


class JobSeekerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "jobseeker":
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")


class CompanyRoleRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "company":
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")


class RedirectAuthenticatedUserMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('index')

