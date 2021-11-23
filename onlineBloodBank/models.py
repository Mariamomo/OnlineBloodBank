from django.db import models


# Create your models here.

class Destination(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=10)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=200)
