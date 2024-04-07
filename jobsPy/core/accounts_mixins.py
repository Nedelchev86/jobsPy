from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy

from jobsPy.jobs.models import Job


class JobSeekerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "jobseeker":
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)
            # return HttpResponseForbidden("You do not have permission to access this page.")


# class CompanyRoleRequiredMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.role == "company":
#             return super().dispatch(request, *args, **kwargs)
#         else:
#             return HttpResponseForbidden("You do not have permission to access this page.")

class CompanyRoleRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "company":
            return super().dispatch(request, *args, **kwargs)
        else:

            return render(request, '403.html', status=403)


class RedirectAuthenticatedUserMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('index')


class JobSeekerOwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.pk != kwargs.get('pk', None):
    #         raise PermissionDenied("You are not allowed to edit this profile.")
    #     return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.jobseeker.pk != kwargs.get('pk', None):
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class CompanyOwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.pk != kwargs.get('pk', None):
    #         raise PermissionDenied("You are not allowed to edit this profile.")
    #     return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.company.pk != kwargs.get('pk', None):
            messages.error(self.request, "You don't have permission to access this page.")
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class JobByCompanyMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        print(self.get_object().user)
        if request.user.pk == self.get_object().user.pk:
            return super().dispatch(request, *args, **kwargs)
        else:

            return render(request, '403.html', status=403)


class JobEditMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):

        if request.user.pk == self.get_object().job_seeker.pk:
            return super().dispatch(request, *args, **kwargs)
        else:

            return render(request, '403.html', status=403)


class CompanyProfileActivationMixin:

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.company.activated:

            messages.warning(request, "Please complete your company profile information before posting a job. Go to: Edit Company")
            return redirect(reverse_lazy('company-dashboard'))
        return super().dispatch(request, *args, **kwargs)


# class JonSeekerProfileActivationMixin:
#
#     def dispatch(self, request, *args, **kwargs):
#         if not self.request.user.jobseeker.activated:
#
#             messages.warning(request, "Please complete your company profile information before posting a job. Go to: Edit Company")
#             return redirect(reverse_lazy('company-dashboard'))
#         return super().dispatch(request, *args, **kwargs)

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Author').exists()

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to access this page.")
        return HttpResponseRedirect(reverse('index'))



class ApplicantOwnerRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        job_pk = self.kwargs.get('pk')
        job = get_object_or_404(Job, pk=job_pk)
        if not request.user == job.user:
            messages.error(self.request, "You don't have permission to access this page.")
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)