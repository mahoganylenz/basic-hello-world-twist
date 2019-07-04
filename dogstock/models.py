from django.db import models
#RIGHT models
class Dogs(models.Model):
    dogId = models.CharField(max_length=100, primary_key=True)
    dogName = models.CharField(max_length=30)  
    dogBreed = models.CharField(max_length=30) 
    dogAge = models.CharField(max_length=30) 
    ownerId= models.CharField(max_length=30) 

class Owners(models.Model):
    ownerId = models.ManyToManyField ('Owners')
    ownerFName = models.CharField(max_length=30) 
    ownerLName = models.CharField(max_length=30) 

class Stocks(models.Model):
    investorId= models.IntegerField(primary_key=True)
    stock_symbol = models.CharField(max_length=30) 
    num_of_shares = models.IntegerField()
    purch_price = models.IntegerField()
    current_val = models.IntegerField()
    purch_date = models.DateTimeField()

class Dogs2(models.Model):
    dogId = models.CharField(max_length=100, primary_key=True)
    dogName = models.TextField(max_length=60)  
    dogBreed = models.TextField(max_length= 100) 
    dogAge = models.TextField(max_length=50) 
    ownerId= models.TextField(max_length=100) 
