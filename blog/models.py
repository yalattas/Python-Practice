from django.db import models
import datetime
from app.models import User

# Create your models here.
class Post (models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=800)
    description = models.TextField(blank=True, null=True)
    # Needs to import User from models in order to use it
    user = models.ForeignKey(User, on_delete=models.CASCADE)