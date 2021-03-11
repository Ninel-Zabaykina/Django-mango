from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40, blank=False, unique=True)
    descriptions = models.TextField(default='', max_length=500, blank=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    published = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(blank=True, null=True)
    cover = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,
                              blank=True, null=True)