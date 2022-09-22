from django.forms import ModelForm
from .models import Disease
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields= '__all__'
        exclude = ['sickness']
        widgets = {
            'symptom1' : forms.Select(attrs={'class':'form-control'}),
            'symptom2' : forms.Select(attrs={'class':'form-control'}),
            'symptom3' : forms.Select(attrs={'class':'form-control'}),
            'symptom4' : forms.Select(attrs={'class':'form-control'}),
            'symptom5' : forms.Select(attrs={'class':'form-control'}),
            'symptom6' : forms.Select(attrs={'class':'form-control'}),
            'symptom7' : forms.Select(attrs={'class':'form-control'})
            
        }


        



class UserCreateForm(UserCreationForm):
    

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserForm(ModelForm):
    class Meta:
        model = User
        fields=['username', 'email','password']

        widgets = {
            'username':  forms.TextInput(attrs={'class':'form-control'}),
            'email':  forms.TextInput(attrs={'class':'form-control'}),
            'password':  forms.TextInput(attrs={'class':'form-control'}),

        }
       