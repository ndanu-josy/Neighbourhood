from django.contrib import admin
from .models import Post, Neighbourhood, Profile, Business
# Register your models here.

admin.site.register(Post)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
