from django.db import models
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

class User(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(default=datetime.datetime.now())

    username = models.EmailField()

    def __str__(self):
        return self.username + '-' + str(self.id)