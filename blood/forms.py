from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','hospitalID','bloodgroup','unit']
class RequestFormForHospital(forms.ModelForm):
    class Meta:
        model=models.BloodRequestByHospital
        fields=['hospitalName','hospitalID','bloodgroup','unit']
