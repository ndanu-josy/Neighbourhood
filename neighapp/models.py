from django.db import models
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField
# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name= models.CharField(max_length=80)
    neighbourhood_location = models.CharField(max_length=80)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adminstrator')

    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, id):
        return cls.objects.filter(id=id)

    def update_neighbourhood(self):
        name = self.neighbourhood_name
        self.neighbourhood_name = name

    @classmethod
    def update_occupants(cls, id):
        occupant= cls.objects.get(id=id)
        count = occupant.occupants_count + 1
        cls.objects.filter (id=id). update(occupants_count = count )

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= CloudinaryField('profile-pic')
    bio = models.TextField(max_length=100) 
    general_location= models.CharField(max_length=100)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user
    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete() 

class Business(models.Model): 
    business_name= models.CharField(max_length=100)
    user= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='business_owner')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)
    business_email = models.CharField(max_length=50)


    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()   

    def delete_business(self):
        self.delete()   

    @classmethod
    def find_business(cls, business_id):
            return cls.objects.filter(id=business_id)

    def update_business(self):
        name = self.business_name
        self.business_name = name         