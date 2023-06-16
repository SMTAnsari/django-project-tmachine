from django.contrib import admin
from .models import *

class UserData(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']

admin.site.register(Feature, UserData)

