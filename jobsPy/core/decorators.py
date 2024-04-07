from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


def job_seeker_activated_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        if request.user.is_authenticated and request.user.role == 'jobseeker':
            # Check if the user is activated
            if request.user.jobseeker.activated:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "Please complete your profile information before apply for a job. Go to: Edit Profile")
                return redirect(reverse_lazy('job seeker dashboard'))  # Redirect to the home page or another appropriate URL
        else:

            messages.error(request, "You must be a job seeker to perform this action.")
            return redirect(reverse_lazy('index'))  # Redirect to the home page or another appropriate URL

    return _wrapped_view