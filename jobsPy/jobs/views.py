from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from jobsPy.core.accounts_mixins import CompanyRoleRequiredMixin


class JobCreateView(LoginRequiredMixin, CompanyRoleRequiredMixin, CreateView):
    template_name = "create_job.html"
    form_class = CreateJobForms
    extra_context = {"title": "Post New Job"}
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AllJobsView(ListView):
    model = Job
    template_name = "browsejobs.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # If a search query is present, filter the queryset by job title
            return Job.objects.filter(Q(title__icontains=query))
        else:
            # If no search query, return all jobs
            return Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context['search_query'] = self.request.GET.get('q', '')
        return context