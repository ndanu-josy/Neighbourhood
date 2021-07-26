from django.db import models
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=200)
    neighbourhood_location = models.CharField(max_length=200)
    neighbourhood_description = models.TextField(max_length=500, blank=True)
    neighbourhood_photo = CloudinaryField('photo', default='photo')
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='admin')
    def __str__(self):
        return self.neighbourhood_name
      
    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)
        
    def update_hood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNo = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def update_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #     instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id) 

class Business(models.Model): 
    business_name= models.CharField(max_length=100)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='business_owner')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)
    business_email = models.CharField(max_length=50)


    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()   

    def delete_business(self):
        self.delete()   

    @classmethod
    def find_business(cls, search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses
    

    def update_business(self):
        name = self.business_name
        self.business_name = name   


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='poster')
    post_category = models.CharField(max_length=120)
    post_title = models.CharField(max_length=100, null=True)
    post_description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)   
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbourhood_post')      

    def __str__(self):
        return self.post_title

    def create_post(self):
        self.save()   

    def delete_post(self):
        self.delete()            