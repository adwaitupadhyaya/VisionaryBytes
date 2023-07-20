from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

User = get_user_model()

class UserType(models.Model):
    user_type_choices=(
        ('client','client'),
        ('serviceprovider','serviceprovider')
    )
    user_type=models.CharField(max_length=20,null=True,blank=True, choices=user_type_choices)
    user=models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()


class ServiceProviderModel(models.Model):

    types = (
        ("Electrician", "electrician" ),
        ("IT", "IT" ),
        ("Plumbing", "Plumbing" ),
        ("Gardening", "Gardening" ),
        ("Painting", "Painting" ),
        ("Carpentry", "Carpentry" ),
    )
    full_name = models.CharField(max_length=100, null = True, blank = True)
    phone_number = models.CharField(max_length=10,null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null = True, blank = True)
    citizenship_image = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
    email = models.EmailField(max_length=254)
    cv = models.FileField(upload_to='media', max_length=255)
    type_of_service = models.CharField(max_length=20, null = True, blank = True, choices=types)
    threshold = models.FloatField(default = 0, null = True, blank = "True")
    
    def __str__(self):
        return self.full_name

class ClientRequestsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    technician = models.CharField(max_length=200, null = True, blank = True)
    date_time = models.DateTimeField(auto_now_add=True, null = True, blank = True)

    def __str__(self):
        return str(self.technician)