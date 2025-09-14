from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Prof_form(forms.ModelForm):
    class  Meta:
        model=Profile
        fields=['first','last','about','address','work','waiting_time','price','image','facebook','twitter','google']
        


class UserCreationForms(UserCreationForm):
    class  Meta:
        model=User
        fields=['username','email','password1','password2']

class UpdateProfile(forms.ModelForm):
    class  Meta:
        model=Profile
        fields=['first','last','about','image','address','work','waiting_time','price','facebook','google','twitter']


# class ImageForm(forms.ModelForm):
#        class Meta:
#            model=Image
#            fields=['caption','img']
      
class projectForm(forms.ModelForm):
    class Meta:
        model=project
        fields=['grapher','discription','work']