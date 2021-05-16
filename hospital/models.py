from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hospital(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic/hospital')
    hospitalID=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    hotline=models.CharField(max_length=20, null=False)
    
    @property
    def get_name(self):
        return self.user.username

    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.username
