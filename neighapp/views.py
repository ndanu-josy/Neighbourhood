from django.contrib.auth import login
from neighapp.forms import RegistrationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'index.html')
    
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
        
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 
