from django.conf.urls import include, url
from django.urls.conf import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[  
    url(r'^$',views.index,name='index'),
    url(r'register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'profile/', views.profile, name='profile'),
    url('createHood/', views.create_neighbourhood, name='createHood'),
    path('joinhood/<id>', views.join_neighbourhood, name='joinhood'),   
    url('singleHoodm', views.single_hood, name='singleHood'),
]