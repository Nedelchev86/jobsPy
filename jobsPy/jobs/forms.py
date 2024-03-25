
from django.forms import ModelForm, DateInput, CheckboxInput, ChoiceField, CheckboxSelectMultiple, \
    ModelMultipleChoiceField

from jobsPy.jobs.models import Job, Applicant


class CreateJobForms(ModelForm):

    # tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.order_by('name'),widget=forms.SelectMultiple)

    class Meta:
        model = Job
        fields = ['title', 'category','seniority', 'description',   'vacancy', 'location', 'job_type', 'salary',  'deadline',
                  'job_image', 'needed_skills']
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'}),
            # 'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # needed_skills = ModelMultipleChoiceField(
    #     queryset=Skills.objects.all(),
    #     widget=CheckboxSelectMultiple,
    #     required=False
    #     )

    def __init__(self, *args, **kwargs):
        super(CreateJobForms, self).__init__(*args, **kwargs)
        self.fields['salary'].widget.attrs['placeholder'] = 'exp:50,000-80,000'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            # self.fields['is_published'].widget.attrs['class'] = 'form-check-input'
            # self.fields['is_closed'].widget.attrs['class'] = 'form-check-input'
        # self.fields["needed_skills"].widget.attrs['class'] = "form-check"




class ApplyForJobForms(ModelForm):

    class Meta:
        model = Applicant
        fields = ("job",)


class EditeJobForm(CreateJobForms):
    class Meta:
        model = Job
        fields = ['title',  'category', 'seniority', 'description',  'vacancy', 'location', 'job_type', 'salary',  'deadline',
                  'job_image', "is_published", "needed_skills"]
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'}),
            # 'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

statusChoice = {
    1: "Pending",
    2: "Accepted",
    3: "Rejected",
}

class ChangeStatus(ModelForm):
    class Meta:
        model = Applicant
        fields = ["status", "comment"]

    status = ChoiceField(choices=statusChoice)


