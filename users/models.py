
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(default='profile_pic/1.png', upload_to='profile_pic')


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

# Create your models here.
