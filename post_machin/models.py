from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PostMachin(models.Model):
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.adress} {self.city}'

    def __repr__(self):
        return f'{self.adress} {self.city}'



class Locker(models.Model):
    size = models.ImageField()
    post_machin = models.ForeignKey(PostMachin, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)




