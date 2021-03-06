from django.db import models
import datetime
from app.models import User

# Create your models here.
class Post (models.Model):
    # id = models.UUIDField(primary_key=True, editable=False)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    modified_at = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=800)
    description = models.TextField(blank=True, null=True)
    # Needs to import User from models in order to use it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + '-' + str(self.id)