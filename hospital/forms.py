from django import forms
from django.contrib.auth.models import User
from . import models


class HospitalUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['password','username']
        widgets={
            'password':forms.PasswordInput()
        }

class HospitalForm(forms.ModelForm):
    class Meta:
        model=models.Hospital
        fields=['hospitalID','address','hotline','profile_pic']