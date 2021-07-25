from neighapp.models import Business, Neighbourhood, Post, UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user  

class profileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'profile_pic', 'bio']        

class userForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model= User
        fields= ['username', 'email']

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('occupants_count', 'admin')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'neighbourhood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')