from django import forms
from .models import Dogs2

class DogForm (forms.ModelForm):
    class Meta:
        model = Dogs2
        fields = ['dogName', 'dogBreed', 'dogAge'] 
        labels = {'text': ''}
        widgets= {'text': forms.Textarea(attrs={'cols': 40})}


    