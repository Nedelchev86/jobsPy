from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from jobsPy.core.accounts_mixins import JobSeekerRequiredMixin, JobSeekerOwnerRequiredMixin, JobEditMixin
from jobsPy.jobs.models import FavoriteJob, Applicant, Skills
from jobsPy.jobseekers.forms import EditProfileFrom, EducationForm, WrokExperienceForm
from jobsPy.jobseekers.models import JobSeeker, Education, Experience

userModel = get_user_model()
# Create your views here.


class JobSeekerDashboard(LoginRequiredMixin, JobSeekerRequiredMixin, TemplateView):
    template_name = "job_seekers/jobseeker_dashboard.html"

    def get_context_data(self, **kwargs):

        all_favourite = FavoriteJob.objects.filter(user_id=self.request.user.pk).count()
        all_jobs_apply = Applicant.objects.filter(user_id=self.request.user.pk).count()
        all_jobs_pending = Applicant.objects.filter(user_id=self.request.user.pk).filter(status=1).count()
        all_jobs_accepted = Applicant.objects.filter(user_id=self.request.user.pk).filter(status=2).count()
        all_jobs_rejected = Applicant.objects.filter(user_id=self.request.user.pk).filter(status=3).count()


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
    template_name = "job_seekers/all_jobseekers.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(activated=True)
        city = self.request.GET.get('city')
        if city:
            queryset = queryset.filter(city__icontains=city)
        skill_name = self.request.GET.get('skill')
        if skill_name:
            queryset = queryset.filter(skills__name=skill_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skills.objects.all()
        return context

    # def get_queryset(self):
    #     # Use prefetch_related to fetch all related languages for each JobSeeker
    #     print(JobSeeker.objects.prefetch_related('languages').all())
    #     return JobSeeker.objects.prefetch_related('languages').all()


class JobSeekerDetails(DetailView):
    model = JobSeeker
    template_name = "job_seekers/job_seekers_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skills.objects.all()
        return context


class EditProfile(JobSeekerOwnerRequiredMixin, UpdateView):
    model = JobSeeker
    template_name = "job_seekers/edit_profile.html"
    form_class = EditProfileFrom
    success_url = reverse_lazy("job seeker dashboard")

    # def get_context_data(self, **kwargs):
    #     contex = super().get_context_data(**kwargs)
    #     print(self.request.user.pk)
    #     jobseeker = get_object_or_404(JobSeeker, pk=self.request.user.jobseeker.pk)
    #     education = jobseeker.educations.all()
    #     if education:
    #         contex["educations"] = education
    #     return contex


class FavouriteJobs(LoginRequiredMixin, JobSeekerRequiredMixin, ListView):
    template_name = "job_seekers/favourite_jobs.html"

    def get_queryset(self):
        return FavoriteJob.objects.filter(user=self.request.user).select_related('job')


class ApplyJobs(LoginRequiredMixin, JobSeekerRequiredMixin, ListView):
    template_name = "job_seekers/apply-jobs.html"

    def get_queryset(self):
        return Applicant.objects.filter(user_id=self.request.user.pk).all()


class AddEducation(CreateView):
    model = Education
    template_name = "job_seekers/add_education.html"
    form_class = EducationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        jobseeker_pk = self.kwargs['pk']
        jobseeker = get_object_or_404(JobSeeker, pk=jobseeker_pk)
        # Set the job_seeker field and save the form
        form.instance.job_seeker = jobseeker
        return super().form_valid(form)

    def get_success_url(self):
        # return reverse_lazy('edit-profile', kwargs={'pk': self.kwargs['pk']})
        return reverse_lazy('job seeker dashboard')


class EditEducation(JobSeekerRequiredMixin, JobEditMixin, UpdateView):
    model = Education
    template_name = "job_seekers/edit_education.html"
    form_class = EducationForm

    def get_success_url(self):
        # return reverse_lazy('edit-profile', kwargs={'pk': self.kwargs['pk']})
        return reverse_lazy('job seeker dashboard')


class AddWorkExperience(CreateView):
    # model = Experience
    template_name = "job_seekers/add_work_experience.html"
    form_class = WrokExperienceForm

    def form_valid(self, form):
        jobseeker_pk = self.kwargs['pk']
        jobseeker = get_object_or_404(JobSeeker, pk=jobseeker_pk)
        # Set the job_seeker field and save the form
        form.instance.job_seeker = jobseeker
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('job seeker dashboard')


class EditWorkExperience(JobSeekerRequiredMixin, JobEditMixin, UpdateView):
    model = Experience
    template_name = "job_seekers/edit_edit_work_experience.html"
    form_class = WrokExperienceForm

    def get_success_url(self):
        # return reverse_lazy('edit-profile', kwargs={'pk': self.kwargs['pk']})
        return reverse_lazy('job seeker dashboard')


class JobSeekerDeleteView(LoginRequiredMixin, DeleteView):
    model = userModel
    template_name = "job_seekers/delete_profile.html"
    success_url = reverse_lazy('deleted_success')


    def get_object(self, queryset=None):
        # Return the JobSeeker instance for the current logged-in user
        return self.request.user


class ProfileDeletedView(TemplateView):
    template_name = "job_seekers/profile_deleted.html"
