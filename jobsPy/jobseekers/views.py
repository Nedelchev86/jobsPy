from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from jobsPy.core.accounts_mixins import JobSeekerRequiredMixin
from jobsPy.jobs.models import FavoriteJob, Applicant
from jobsPy.jobseekers.forms import EditProfileFrom
from jobsPy.jobseekers.models import JobSeeker


# Create your views here.

class JobSeekerDashboard(LoginRequiredMixin, JobSeekerRequiredMixin, TemplateView):
    template_name = "job_seekers/jobseeker_dashboard.html"


    def get_context_data(self, **kwargs):

        all_favourite = FavoriteJob.objects.filter(user_id=self.request.user.pk).count()
        all_jobs_apply = Applicant.objects.filter(user_id=self.request.user.pk).count()
        all_jobs_pending = Applicant.objects.filter(user_id=self.request.user.pk).filter(status= 1).count()
        all_jobs_accepted = Applicant.objects.filter(user_id=self.request.user.pk).filter(status= 2).count()
        all_jobs_rejected = Applicant.objects.filter(user_id=self.request.user.pk).filter(status= 3).count()



#         job_creator_jobs = Job.objects.filter(user=self.request.user)
#         all_favourite = FavoriteJob.objects.filter(job__in=job_creator_jobs).count()
#         user_jobs = Job.objects.filter(user=self.request.user)
#
#         job_count = FavoriteJob.objects.filter(job__in=job_creator_jobs).count()
#
#         job_for_this_user = Job.objects.filter(user=self.request.user, is_published=True)
#
#
# # ChatGPT get all applicant for current logged user
#         all_applicant = (
#             Applicant.objects.filter(job__user=self.request.user, job__is_published=True)
#             .values('user')
#             .count()
#         )
#
        context = super().get_context_data(**kwargs)
#         context['user_jobs'] = user_jobs
#         context['job_count'] = job_count
        context['all_favourite'] = all_favourite
        context['all_jobs_apply'] = all_jobs_apply
        context['all_jobs_pending'] = all_jobs_pending
        context['all_jobs_rejected'] = all_jobs_rejected
        context['all_jobs_accepted'] = all_jobs_accepted
        return context

class AllEmployees(ListView):
    model = JobSeeker
    template_name = "all_employers.html"

    # def get_queryset(self):
    #     # Use prefetch_related to fetch all related languages for each JobSeeker
    #     print(JobSeeker.objects.prefetch_related('languages').all())
    #     return JobSeeker.objects.prefetch_related('languages').all()


class JobSeekerDetails(DetailView):
    model = JobSeeker
    template_name = "jobseekers_details.html"



class EditProfile(UpdateView):
    model = JobSeeker
    template_name = "job_seekers/edit_profile.html"
    form_class = EditProfileFrom
    success_url = reverse_lazy("index")


    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        print(self.request.user.pk)
        jobseeker = get_object_or_404(JobSeeker, pk=self.request.user.jobseeker.pk)
        education = jobseeker.educations.all()
        if education:
            contex["educations"] = education
        return contex


class FavouriteJobs(LoginRequiredMixin, JobSeekerRequiredMixin, ListView):
    template_name = "favourite_jobs.html"

    def get_queryset(self):
        return FavoriteJob.objects.filter(user=self.request.user).select_related('job')


class ApplyJobs(LoginRequiredMixin, JobSeekerRequiredMixin, ListView):
    template_name = "apply-jobs.html"

    def get_queryset(self):
        return Applicant.objects.filter(user_id=self.request.user.pk).all()