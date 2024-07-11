from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PostMachin(models.Model):
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Locker(models.Model):
    size = models.ImageField()
    post_machin = models.ForeignKey(PostMachin)
    status = models.BooleanField(default=False)



