from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # jobseekers = JobSeeker.objects.all().count()
        # company = CompanyProfile.objects.all().count()
        # jobs = Job.objects.all().count()
        # last_jobs = Job.objects.all().order_by('pk')[:4]


        # context["jobseekers"] = jobseekers
        # context["company"] = company
        # context["coutries"] = jobs
        # context["last_jobs"] = last_jobs
        # context["title"] = "JobsPy - Your Future Begins Here"
        return context