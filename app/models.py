from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Visitor (models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(default=datetime.datetime.now())

    email = models.EmailField()
    location = models.CharField(
        choices=(
            ('SA', 'Saudi Arabia'),
            ('FR', 'Out of Saudi Arabia'),
            ('NA','Prefer not to say'),
        ),
        default='Prefer not to say',
        max_length=250
    )
    img = models.ImageField(upload_to= 'media')

    def __str__(self):
        return self.email + '-' + str(self.id)

# Require import from Django auth #from django.contrib.auth.models import AbstractUser
'''class CustomUser(User):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(default=datetime.datetime.now())
    user_name =  models.OneToOneField(User, on_delete=models.CASCADE)
    
    user = models.CharField(
        ('user'), unique=True, max_length=85
    )
    email_address = models.EmailField(('email address'), unique=True)
    class Meta:
        ordering = ('user','email address','password')

    def __str__(self):
        return self.user
'''
class User(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(default=datetime.datetime.now())

    username = models.EmailField()

    def __str__(self):
        return self.username + '-' + str(self.id)