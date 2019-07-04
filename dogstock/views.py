from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

from .models import Dogs
from .models import Owners
from .models import Stocks
from .forms import DogForm

def home(request):
    """Home Page for Dog"""
    dogs = Dogs.objects.all()
    owners = Owners.objects.all()
    return render(request,'home.html',{'dogs': dogs, 'owners': owners})


def dogowner(request):
    try:
        stocks = Dogs.objects.all() 
    except Dogs.DoesNotExist:
        raise Http404('Dogs not found')

    context = {'dogowner': stocks}    
    return render(request,'dogowner.html',context)

def new_dog(request):
    """Add a new dog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = DogForm()
    else:
        #POST data submitted; process data
        form = DogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dogstock:Dogs2'))
    context = {'form': form}
    return render(request, 'new_dog.html', context ) 
    