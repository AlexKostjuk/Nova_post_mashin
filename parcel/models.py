from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Parcel(models.Model):
    recipient = models.ForeignKey(User)
    sender = models.ForeignKey(User)
    size =models.ImageField()
    post_machin = models.ForeignKey(PostMacine)
    order_date_time = models.DateTimeField('date published')
    open_date_time = models.DateTimeField('date published')
    status = models.BooleanField(default=0)

