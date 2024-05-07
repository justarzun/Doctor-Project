from django.db import models

# Create your models here.
class ContactForm(models.Model):
    message = models.CharField(max_length=250)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    


    def __str__(self):
        return self.message + self.name + self.email + self.subject 

class BookingForm(models.Model):
    
    name = models.CharField(max_length=15)
    phone = models.IntegerField(max_length=104)
    select = models.CharField(max_length=10)
    email = models.CharField(max_length=15)
    message = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name + self.email + self.select + self.message 

    def __int__(self):
        return self.phone 