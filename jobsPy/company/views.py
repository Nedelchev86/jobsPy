from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class CompanyDashboard(LoginRequiredMixin, CompanyRoleRequiredMixin, TemplateView):
    template_name = "company_dashboard.html"


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