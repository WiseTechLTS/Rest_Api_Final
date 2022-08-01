from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    price = models.DecimalField()
    inventory_quantity = models.IntegerField()
