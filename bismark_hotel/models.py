from django.db import models

# Create your models here.
class Room(models.Model):
    image = models.ImageField(upload_to = 'pics')
    room_type = models.CharField(max_length = 100)
    description = models.TextField( )
    price = models.IntegerField()
    

class Booked(models.Model):
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    email = models.EmailField(max_length=254)
    mobile_phone = models.IntegerField()
    address = models.CharField(max_length = 100)
    room_type = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    checkin_date = models.DateField(auto_now=False, auto_now_add=False)
    checkout_date = models.DateField(auto_now=False, auto_now_add=False)
    number_of_guests = models.IntegerField()
    number_of_rooms = models.IntegerField()
    price = models.IntegerField()
    
class Contact(models.Model):
    full_name =  models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length = 100)
    message = models.TextField()




    
