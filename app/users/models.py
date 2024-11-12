from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

    class Meta:
        db_table = 'user'
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.email