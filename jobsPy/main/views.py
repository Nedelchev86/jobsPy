from django.views.generic import TemplateView, ListView

from jobsPy.jobs.models import Category, Job


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


class Contact(TemplateView):
    template_name = "core/contacts.html"


class JobsCategory(ListView):
    model = Job
    template_name = "jobs/jobs_list.html"


    def get_queryset(self):
        # Get the category slug from the URL
        category_slug = self.kwargs.get('category_slug')

        # Retrieve the Category object based on the slug
        category = Category.objects.get(slug=category_slug)

        # Filter jobs based on the selected category
        queryset = Job.objects.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the selected category to the template
        context['selected_category'] = Category.objects.get(slug=self.kwargs.get('category_slug'))
        context["category"] = Category.objects.all()
        return context
