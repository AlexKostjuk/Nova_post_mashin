from django.contrib.auth.models import User
from django.db import models

from post_machin.models import PostMachin


# Create your models here.
class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.ImageField()
    post_machin = models.ForeignKey(PostMachin, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField('date published')
    open_date_time = models.DateTimeField('date published')
    status = models.BooleanField(default=False)




