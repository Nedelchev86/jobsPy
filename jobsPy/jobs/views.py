from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View

from jobsPy.company.models import CompanyProfile
from jobsPy.core.accounts_mixins import CompanyRoleRequiredMixin
from jobsPy.jobs.forms import CreateJobForms, EditeJobForm, ApplyForJobForms, ChangeStatus
from jobsPy.jobs.models import Job, Category, Applicant, FavoriteJob


class JobCreateView(LoginRequiredMixin, CompanyRoleRequiredMixin, CreateView):
    template_name = "jobs/create_job.html"
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
    template_name = "jobs/jobs_list.html"

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


class JobDetails(DetailView):
    template_name = "jobs/job-details.html"
    model = Job

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if self.request.user.is_anonymous:
            return context

        job = context['object']

        context["already_in_favourite"] = FavoriteJob.objects.filter(user=self.request.user, job=job).exists()
        context["already_apply"] = Applicant.objects.filter(user=self.request.user, job=job).exists()
        context["status"] = Applicant.objects.filter(user=self.request.user, job=job)
        # Access the CompanyProfile through the user's ID
        company_profile = CompanyProfile.objects.get(user_id=job.user_id)
        context['company'] = company_profile

        return context


class EditJob(LoginRequiredMixin, CompanyRoleRequiredMixin, UpdateView):
    model = Job
    form_class = EditeJobForm
    template_name = "jobs/edit-job.html"

    def get_success_url(self):

        return reverse_lazy("job_details",  kwargs={"pk":self.object.pk})


# class AddToFavoritesView(LoginRequiredMixin, View):
#     # @login_required
#     def post(self, request, pk):
#         job = get_object_or_404(Job, id=pk)
#
#         # Check if the job is already in favorites for the current user
#         if FavoriteJob.objects.filter(user=request.user, job=job).exists():
#             # Job is already in favorites, handle this case (e.g., display a message)
#             pass
#         else:
#             # Job is not in favorites, add it to the favorites
#             FavoriteJob.objects.create(user=request.user, job=job)
#
#         return redirect('job_details', pk)

# class AddToFavoritesView(LoginRequiredMixin, CreateView):
#     model = FavoriteJob
#     template_name = 'add_to_favorites.html'
#     fields = []
#
#     def form_valid(self, form):
#         job = get_object_or_404(Job, pk=self.kwargs['pk'])
#         form.instance.user = self.request.user
#         form.instance.job = job
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         job = get_object_or_404(Job, pk=self.kwargs['pk'])
#         return reverse_lazy("job_details",  kwargs={"pk": job.pk})


class RemoveFromFavoritesView(LoginRequiredMixin, View):

    def post(self, request, pk):
        job = get_object_or_404(Job, id=pk)

        # Check if the job is in favorites for the current user
        favorite_job = FavoriteJob.objects.filter(user=request.user, job=job).first()

        if favorite_job:
            # Job is in favorites, remove it
            favorite_job.delete()

        return redirect('job_details', pk)


def apply_for_job(request, pk):
    job = get_object_or_404(Job, id=pk)

    if request.user.is_authenticated and request.user.role == 'jobseeker':

        # Check if the user has already applied for this job
        if not Applicant.objects.filter(user=request.user, job=job).exists():
            # Create an Applicant instance and save it to the database
            Applicant.objects.create(user=request.user, job=job)
            # You can also use a form to save additional data if needed
            form = ApplyForJobForms(request.POST or None)
            if form.is_valid():
                applicant = form.save(commit=False)
                applicant.user = request.user
                applicant.job = job
                applicant.save()

    return redirect('job_details', pk=job.id)


@login_required
def add_to_favorites(request, pk):
    if request.user.role != 'jobseeker':
        return redirect('job_details', pk=pk)

    job = get_object_or_404(Job, pk=pk)

    # Check if the job is not already in favorites
    if not FavoriteJob.objects.filter(user=request.user, job=job).exists():
        FavoriteJob.objects.create(user=request.user, job=job)

    return redirect('job_details', pk=pk)


class ChangeStatus(UpdateView):
    model = Applicant

    template_name = "jobs/change_status.html"
    form_class = ChangeStatus

    def get_success_url(self):
        return reverse_lazy("applicant_list", kwargs={"pk": self.object.job_id})


