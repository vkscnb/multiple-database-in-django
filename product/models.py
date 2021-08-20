from django.db import models
from user.models import Users
# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True,null=True)
    updated_at = models.DateTimeField(null=True, blank=True)
