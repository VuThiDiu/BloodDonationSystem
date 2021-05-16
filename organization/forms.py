from django import forms
from django.db.models import fields
from . import models

class RequestBloodDonationOrganizationForm(forms.ModelForm):
    class Meta:
        model=models.RequestBloodDonationRequest
        fields=['hospitalName','hospitalID','address','startDate','endDate','description']