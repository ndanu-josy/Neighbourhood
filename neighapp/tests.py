from django.test import TestCase
from .models import Neighbourhood, Profile, Business
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User(username="jos", password="jos")
        self.user.save()
        self.neighbourhood= Neighbourhood(neighbourhood_name = "mowlem", neighbourhood_location= "Saika", admin = self.user,neighbourhood_description='off kangundo road')
        self.neighbourhood.save()
        self.profile = Profile(bio='I live here',email='location@gmail.com',user = self.user, neighbourhood = self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

  
    def test_delete_profile(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)


class NeighbourhoodTestClass(TestCase):

    def setUp(self):        
        self.user = User(username='jos')
        self.user.save()
        self.neighbourhood = Neighbourhood(neighbourhood_name='mowlem',neighbourhood_location='Saika',neighbourhood_description="the best",neighbourhood_photo='photo.jpd',admin = self.user)
        self.neighbourhood.save_hood()

    def tearDown(self):
         Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_neighborhood(self):
        self.neighbourhood.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_neighborhood(self):
        self.neighbourhood.save_hood()
        self.neighbourhood.delete_hood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)        


class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User(username="jos", password="jos")
        self.user.save()
        self.neighbourhood= Neighbourhood(neighbourhood_name = "mowlem", neighbourhood_location= "Saika", admin = self.user,neighbourhood_description='off kangundo road')
        self.neighbourhood.save()
        self.business = Business(business_name='milkkiosk', business_email='milk@gmail.com', neighbourhood_id='self.neighbourhood')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_save_business(self):
        self.business.create_business()
        biz = Business.objects.all()
        self.assertTrue(len(biz) > 0)        