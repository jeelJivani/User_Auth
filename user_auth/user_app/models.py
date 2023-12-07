from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
