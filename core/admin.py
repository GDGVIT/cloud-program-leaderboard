from django.contrib import admin

# Register your models here.
from .models import UserModel

admin.site.register(UserModel)