from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Event


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_time', 'end_time', 'is_active']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }