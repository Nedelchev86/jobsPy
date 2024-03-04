from django.forms import ModelForm

from jobsPy.company.models import CompanyProfile


class EditCompany(ModelForm):

    # tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.order_by('name'),widget=forms.SelectMultiple)

    class Meta:
        model = CompanyProfile
        exclude = ["user"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     self.fields['salary'].widget.attrs['placeholder'] = 'exp:50,000-80,000'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    #         self.fields['deadline'].widget.attrs['class'] = 'col-md-6'
    #         self.fields['clear'].widget.attrs['class'] = 'form-check-input'
