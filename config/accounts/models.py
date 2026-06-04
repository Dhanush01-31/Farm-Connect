from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model.
class User(AbstractUser):

    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username