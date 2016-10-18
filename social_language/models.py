from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import os

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('avatar', str(instance.id), filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to=get_image_path, blank=True, null=True)
