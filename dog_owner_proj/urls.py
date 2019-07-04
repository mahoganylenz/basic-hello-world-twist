"""dog_owner_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url 

from dogstock import views


urlpatterns = [
    url('admin/', admin.site.urls),
    #Home Page
    # url(r'^$', include('dogstock.urls',namespace='dogstock'))
    url(r'^home', views.home, name='home'),
    #Page for adding a new dawg
    url(r'^new_dog.html', views.new_dog, name='new_dog'),

    url(r'^dogowner.html', views.dogowner, name='dogowner'),
    
]

"""Defines URL patterns for dog owner stocks"""
