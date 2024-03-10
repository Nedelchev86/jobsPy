from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    # ROLE_CHOICES = (
    #     ('jobseeker', 'Job Seekeker'),
    #     ('company', 'Company'),
    # )
    #
    # role = ChoiceField(choices=ROLE_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs.update({
                 'placeholder': 'Enter your email'})

        self.fields['password1'].widget.attrs.update({
                 'placeholder': 'Enter your password'})

        self.fields['password2'].widget.attrs.update({
                 'placeholder': 'Enter your password'})

        self.fields['role'].label = "Profile type"

    # def save(self, commit=True):
    #     # user = super().save(commit=False)
    #     user = super().save(commit=commit)
    #     role = self.cleaned_data['role']
    #
    #     if role == 'jobseeker':
    #         profile = JobSeeker(user=user)
    #     elif role == 'company':
    #         profile = CompanyProfile(user=user)
    #     else:
    #         raise ValueError('Invalid role selected')
    #
    #     if commit:
    #         profile.save()
    #
    #     return user

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "role"]


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs.update({
                 'placeholder': 'Enter your email'})

        self.fields['password'].widget.attrs.update({
                 'placeholder': 'Enter your password'})


class ChangePassword(PasswordChangeForm):
    class Meta:
        model = UserModel
