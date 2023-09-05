from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Media/product_image')
    price=models.IntegerField()

class Members(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Media/Members_image')
    Designation=models.CharField(max_length=50)

class Teamoffer(models.Model):
    image=models.ImageField(upload_to='Media/Members1_image')
    about=models.CharField(max_length=200)
    name=models.CharField(max_length=50)
    profession=models.CharField(max_length=50)

class LatestA(models.Model):
    image=models.ImageField(upload_to='Media/Web_image')

class LatestB(models.Model):
    image=models.ImageField(upload_to='Media/web1_image')


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Address=models.TextField()
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.IntegerField()
    Phone=models.IntegerField()
    Email=models.EmailField(max_length=50)
 
    def __str__(self):
        return self.First_Name
    

class Orderitem(models.Model):
    Order=models.ForeignKey(Order,on_delete=models.CASCADE)
    Product=models.CharField(max_length=40)
    image=models.ImageField(upload_to='media/order')
    qunatity=models.IntegerField()
    price=models.FloatField()
    total=models.IntegerField()
    paid=models.BooleanField(default=False)

class Email(models.Model):
    Email=models.EmailField(max_length=50)

class Contact(models.Model):
    Name=models.CharField(max_length=50)
    Email1=models.EmailField(max_length=40)
    Subject=models.CharField(max_length=200)
    Message=models.CharField(max_length=250)
    
class Leave_message(models.Model):
    Name=models.CharField(max_length=50)
    Email1=models.EmailField(max_length=40)
    Website=models.CharField(max_length=200)
    Comment=models.CharField(max_length=250)