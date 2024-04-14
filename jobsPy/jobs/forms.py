from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, DateInput, CheckboxInput, ChoiceField, CheckboxSelectMultiple, \
    ModelMultipleChoiceField, CharField

from jobsPy.jobs.models import Job, Applicant, Skills


class CreateJobForms(ModelForm):
    required_css_class = 'required'
    # tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.order_by('name'),widget=forms.SelectMultiple)

    class Meta:
        model = Job
        fields = ['title', 'category','seniority', 'description', 'responsibilities', 'benefits',  'vacancy', 'location', 'job_type', 'salary',  'deadline',
                  'job_image', 'needed_skills']
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'}),
            'description': CharField(widget=CKEditorWidget()),
            'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
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





class ApplyForJobForms(ModelForm):

    class Meta:
        model = Applicant
        fields = ("job",)


class EditeJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title',  'category', 'seniority', 'description', 'responsibilities', 'benefits', 'vacancy', 'location', 'job_type', 'salary',  'deadline',
                  'job_image', "needed_skills", "is_published"]

        widgets = {
            'deadline': DateInput(attrs={'type': 'date'}),
            'description': CharField(widget=CKEditorWidget()),
            'needed_skills': CheckboxSelectMultiple(attrs={'class': 'form-check'}),
            'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # needed_skills = ModelMultipleChoiceField(
    #     queryset=Skills.objects.all(),
    #     widget=CheckboxSelectMultiple,
    #     required=False
    #     )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salary'].widget.attrs['placeholder'] = 'exp:50,000-80,000'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields["is_published"].widget.attrs['class'] = "form-check"
        self.fields["needed_skills"].widget.attrs['class'] = "form-check"

statusChoice = {
    1: "Pending",
    2: "Accepted",
    3: "Rejected",
}

class ChangeStatusForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ["status", "comment"]

    status = ChoiceField(choices=statusChoice)


