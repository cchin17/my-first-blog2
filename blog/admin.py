from django.contrib import admin
from .models import Post #import post model
# Register your models here.

admin.site.register(Post) #to make post model visible on the admin page, need to register model
