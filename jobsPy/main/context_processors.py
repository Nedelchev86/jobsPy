from jobsPy.main.forms import SubscriberForm


def subscription_form(request):
    return {'subscription_form': SubscriberForm()}
