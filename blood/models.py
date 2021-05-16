from datetime import date
from django.db import models
from patient import models as pmodels
from donor import models as dmodels
from hospital import models as hmodels
class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    request_by_patient=models.ForeignKey(pmodels.Patient,null=True,on_delete=models.CASCADE)
    request_by_donor=models.ForeignKey(dmodels.Donor,null=True,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=30)
    patient_age=models.PositiveIntegerField()
    reason=models.CharField(max_length=500)
    hospitalID=models.CharField(max_length=30)
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status_hospital=models.CharField(max_length=20, default="Pending")
    status=models.CharField(max_length=20,default="Pending")
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.bloodgroup
class BloodRequestByHospital(models.Model):
    request_by_hospital=models.ForeignKey(hmodels.Hospital,null=True,on_delete=models.CASCADE)
    hospitalName=models.CharField(max_length=100, default="")
    hospitalID=models.CharField(max_length=100, default="")
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=30, default="Pending")
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.bloodgroup

        