from neighapp.models import Business, Neighbourhood, Post
from django.contrib.auth import login
from neighapp.forms import BusinessForm, NeighbourHoodForm, RegistrationForm, profileForm, userForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hoods":hoods})

@login_required(login_url='/accounts/login/')
def profile(request):
 
    if request.method == 'POST':
        user_form = userForm(request.POST, instance=request.user)
        profile_form = profileForm(
            request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
    else:        
        profile_form = profileForm(instance=request.user)
        user_form =userForm(instance=request.user)         
    return render(request,'user_profile.html',{"user_form":user_form,"profile_form": profile_form}) 

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


@login_required(login_url='/accounts/login/')
def create_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user
            neighbourhood.save()          
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'create_hood.html', {'form': form})



@login_required(login_url='/accounts/login/')
def join_neighbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('index')  


@login_required(login_url='/accounts/login/')
def leave_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()   
    return redirect('index')



@login_required(login_url='/accounts/login/')
def single_neighbourhood(request, hood_id):
    neighbourhood = Neighbourhood.objects.get(id=hood_id)

    posts = Post.objects.filter(neighbourhood=neighbourhood)
  
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business_form = form.save(commit=False)
            business_form.neighbourhood = neighbourhood
            business_form.user = request.user.profile
            business_form.save()
            return redirect('single-hood', hood_id)
    else:
        form = BusinessForm()
    
    return render(request, 'singlehood.html', { 'neighbourhood': neighbourhood, 
     'form': form,'posts': posts})

