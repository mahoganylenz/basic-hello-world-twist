from django.contrib import admin
from .models import Dogs
from .models import Dogs2
from .models import Stocks


@admin.register(Dogs,Dogs2)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['dogId', 'dogName', 'dogBreed','dogAge','ownerId'] 

