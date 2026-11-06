from django import forms
from Job_portalApp.models import Jobs,Application
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password')


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['resume']