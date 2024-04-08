from django.forms import ModelForm, EmailInput
from jobsPy.main.models import Subscriber, Newsletter


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

        widgets = {
            'email': EmailInput(attrs={
                'class': 'common-input',
                'placeholder': 'Your email address',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Your email address'",
                'required': True,
                'autocomplete': 'email'}),
        }


class NewsletterForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Newsletter
        fields = ['title', 'content']

