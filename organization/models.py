from django.db import models
from hospital import  models as hmodels
import hospital
# Create your models here.

class RequestBloodDonationRequest(models.Model):
    request_by_hospital = models.ForeignKey(hmodels.Hospital, null=True, on_delete=models.CASCADE)
    hospitalName=models.CharField(max_length=100, default="")
    hospitalID=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=500)
    startDate=models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    description=models.CharField(max_length=500)   
    status=models.CharField(max_length=20,default="Pending") 
    def __str__(self):
        return self.description
