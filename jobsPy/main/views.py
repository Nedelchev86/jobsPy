from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, FormView
from jobsPy.company.models import CompanyProfile
from jobsPy.core.accounts_mixins import AuthorRequiredMixin
from jobsPy.jobs.models import Category, Job
from jobsPy.jobseekers.models import JobSeeker
from jobsPy.main.forms import SubscriberForm, NewsletterForm
from jobsPy.main.models import Contact, Subscriber, Newsletter
from jobsPy.main.tasks import send_contact_form_confirmation, send_contact_form_notification_to_team, \
    send_news_notification


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_seekers = JobSeeker.objects.all().count()
        company = CompanyProfile.objects.all().count()
        jobs = Job.objects.all().count()
        # last_jobs = Job.objects.all().order_by('pk')[:4]


        context["job_seekers"] = job_seekers
        context["company"] = company
        context["jobs"] = jobs
        # context["last_jobs"] = last_jobs
        context["title"] = "JobsPy - Your Future Begins Here"

        return context


# class Contact(TemplateView):
#     template_name = "core/contacts.html"


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


def custom_403(request, exception):
    return render(request, '403.html')


class ContactFrom(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'phone', 'message']
    success_url = reverse_lazy('index')
    template_name = "core/contacts.html"

    def form_valid(self, form):
        response = super().form_valid(form)

        send_contact_form_confirmation.delay(form.instance.name, form.instance.email,)

        send_contact_form_notification_to_team.delay(form.instance.name, form.instance.email, form.instance.subject, form.instance.phone, form.instance.message)

        return response


class SubscribeToNewsletterView(FormView):
    template_name = 'core/subscribe.html'
    form_class = SubscriberForm
    success_url = reverse_lazy('subscribe success')


    def form_valid(self, form):
        email = form.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(self.request, 'Email already subscribed.')
            form.add_error('email', 'Email already subscribed.')
            return self.render_to_response(self.get_context_data(form=form))
        form.save()
        messages.success(self.request, 'Successfully subscribed.')
        return super().form_valid(form)


class SubscribeSuccessView(TemplateView):
    template_name = "core/subscribe-success.html"


class NewsletterCreateView(LoginRequiredMixin, AuthorRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'core/newsletter.html'
    success_url = reverse_lazy('subscribe success')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        send_news_notification.delay(news.title, news.content)
        return super().form_valid(form)