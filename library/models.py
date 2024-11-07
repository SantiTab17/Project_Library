from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    stock = models.IntegerField(null=True, default=0)
    date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)