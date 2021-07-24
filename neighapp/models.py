from django.db import models
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField
# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name= models.CharField(max_length=80)
    neighbourhood_location = models.CharField(max_length=80)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adminstrator')


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= CloudinaryField('profile-pic')
    bio = models.TextField(max_length=100) 
    general_location= models.CharField(max_length=100)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

class Business(models.Model): 
    business_name= models.CharField(max_length=100)
    user= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='business_owner')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)
    business_email = models.CharField(max_length=50)