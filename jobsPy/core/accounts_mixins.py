from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


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


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.pk != kwargs.get('pk', None):
    #         raise PermissionDenied("You are not allowed to edit this profile.")
    #     return super().dispatch(request, *args, **kwargs)


    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)
