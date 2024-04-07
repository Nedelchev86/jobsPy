from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple, CharField, DateInput

from jobsPy.jobs.models import Skills
from jobsPy.jobseekers.models import JobSeeker, Education, Experience


class EditProfileFrom(ModelForm):
    required_css_class = 'required'
    # languages = ModelMultipleChoiceField(
    #                     queryset=Skills.objects.all(),
    #                     label="Language",
    #                     widget=CheckboxSelectMultiple)

    class Meta:
        model = JobSeeker
        exclude = ["user", 'activated']

        widgets = {
            'about': CharField(widget=CKEditorWidget())
            # 'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    skills = ModelMultipleChoiceField(
        queryset=Skills.objects.all(),

        widget=CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields["skills"].widget.attrs['class'] = "form-check"

    # widgets = {
    #     'languages': CheckboxSelectMultiple()
    # }


class EducationForm(ModelForm):
    required_css_class = 'required'
# tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.order_by('name'),widget=forms.SelectMultiple)

    class Meta:
        model = Education
        exclude = ["job_seeker"]

        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }


class WrokExperienceForm(ModelForm):
    required_css_class = 'required'
# tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.order_by('name'),widget=forms.SelectMultiple)

    class Meta:
        model = Experience
        exclude = ["job_seeker"]

        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }
