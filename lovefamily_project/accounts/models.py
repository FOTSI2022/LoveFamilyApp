from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Person(models.Model):
    birth_date=models.DateTimeField(null=True)
    father= models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="father", null=True)
    mother= models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="mother", null=True)
   
    gender=models.CharField(max_length=68, default='male')
   
    #death_date=models.DateTimeField(null=True)
    #phone_number=PhoneNumberField(unique = True, null = True, blank = False)  #a revoir
    phone_number=models.IntegerField(null=True)
    email=models.EmailField(null=True);
    occupation=models.TextField(max_length=200)  #profession
    birth_country=models.TextField(max_length=200, null=True)
    birth_region=models.TextField(max_length=200, null=True)
    history=models.TextField(max_length=100, null=True)
    personallyregister=models.BooleanField(default=True) #elle sera false dans le cas contraire
    profile_image = models.ImageField(upload_to='profile_images/', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
          return f"{self.user.username}"

 
    
