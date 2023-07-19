from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_choices = (
        ("client", "client"),
        ("service provider", "service provider")
    )

    user_type = models.CharField(
        max_length=20, choices=user_type_choices, null=True, blank=True)
