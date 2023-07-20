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
    
