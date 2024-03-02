from django.http import HttpResponseForbidden


class JobSeekerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "jobseeker":
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")