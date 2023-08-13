from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude='__all__'


