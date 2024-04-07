from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField

from jobsPy.company.models import CompanyProfile


class EditCompanyFrom(ModelForm):
    required_css_class = 'required'
    # tags = forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.order_by('name'),widget=forms.SelectMultiple)

    class Meta:
        model = CompanyProfile
        exclude = ['user', 'activated']

        widgets = {
            'description': CharField(widget=CKEditorWidget())
            # 'is_published': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     self.fields['salary'].widget.attrs['placeholder'] = 'exp:50,000-80,000'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    #         self.fields['deadline'].widget.attrs['class'] = 'col-md-6'
    #         self.fields['clear'].widget.attrs['class'] = 'form-check-input'
