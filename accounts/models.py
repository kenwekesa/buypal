from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
  

    def __str__(self):
        return self.user.full_name
