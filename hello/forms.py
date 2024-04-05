from django import forms
from .models import CustomUser




# class SignupForm(UserCreationForm):
#   username = forms.CharField(max_length=30, min_length=8)
#   email = forms.EmailField(max_length=40, min_length=6, help_text='Required')
#   agree_terms = forms.BooleanField()



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['login', 'password']

