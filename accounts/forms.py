from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2',)

        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,

        }