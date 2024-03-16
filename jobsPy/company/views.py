from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DetailView

from jobsPy.company.forms import EditCompany
from jobsPy.company.models import CompanyProfile
from jobsPy.core.accounts_mixins import CompanyRoleRequiredMixin
from jobsPy.jobs.models import Job, Applicant, FavoriteJob


# Create your views here.
class CompanyDashboard(LoginRequiredMixin, CompanyRoleRequiredMixin, TemplateView):
    template_name = "company/company_dashboard.html"


    def get_context_data(self, **kwargs):
        job_creator_jobs = Job.objects.filter(user=self.request.user)
        all_favourite = FavoriteJob.objects.filter(job__in=job_creator_jobs).count()
        user_jobs = Job.objects.filter(user=self.request.user)

        job_count = FavoriteJob.objects.filter(job__in=job_creator_jobs).count()

        job_for_this_user = Job.objects.filter(user=self.request.user, is_published=True)


# ChatGPT get all applicant for current logged user
        all_applicant = (
            Applicant.objects.filter(job__user=self.request.user, job__is_published=True)
            .values('user')
            .count()
        )

        context = super().get_context_data(**kwargs)
        context['user_jobs'] = user_jobs
        context['job_count'] = job_count
        context['all_favourite'] = all_favourite
        context['all_applicant'] = all_applicant
        return context

class CreatedJobs(LoginRequiredMixin, CompanyRoleRequiredMixin, ListView):
    template_name = "company/created-jobs.html"

    def get_queryset(self):
        jobs = Job.objects.filter(user__id=self.request.user.pk).order_by('-id')
        print(jobs)
        return jobs


class EditCompany(LoginRequiredMixin, CompanyRoleRequiredMixin, UpdateView):
    template_name = "company/edit_company.html"
    model = CompanyProfile
    form_class = EditCompany
    # model = CompanyProfile
    # form_class = CreateProfile
    def form_valid(self, form):
        # Ensure you are handling files correctly
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("company-dashboard")


class CompanyApplicant(LoginRequiredMixin, CompanyRoleRequiredMixin, ListView):
    model = Job
    template_name = 'company/jobs_list_aplicant.html'  # Create this template if needed
    context_object_name = 'jobs'

    def get_queryset(self):
        user = self.request.user
        # By ChatGPT
        return Job.objects.filter(user=user, is_published=True).annotate(num_applicants=Count('applicants')).filter(num_applicants__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_applicants_count = {}
        for job in context['jobs']:
            applicants_count = Applicant.objects.filter(job=job).count()
            job_applicants_count[job.id] = applicants_count
        context['job_applicants_count'] = job_applicants_count
        return context


class ApplicantList(LoginRequiredMixin, CompanyRoleRequiredMixin,ListView):
    model = Applicant
    template_name = 'company/applicant_list.html'  # Create this template if needed

    def get_queryset(self):
        job_pk = self.kwargs['pk']
        job = get_object_or_404(Job, pk=job_pk)
        return job.applicants.all()


class CompanyDetails(DetailView):
    model = CompanyProfile
    template_name = "company/company_details.html"


class AllCompany(ListView):
    model = CompanyProfile
    template_name = "company/company.html"
