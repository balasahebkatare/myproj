from django.db import models

# Create your models here.
class Educational(models.Model):
    item = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()

class Electronics(models.Model):
        item = models.CharField(max_length=100)
        price = models.FloatField()
        qty = models.IntegerField()
