from django.conf.urls import url
from django.urls.conf import path
from . import views
urlpatterns=[  
    url(r'^$',views.index,name='index'),

]