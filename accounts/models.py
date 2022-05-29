from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
  

    def __str__(self):
        return self.user.full_name



class News(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    pubdate = models.CharField(max_length=100, null=True, blank=True)
    news_bool = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.title