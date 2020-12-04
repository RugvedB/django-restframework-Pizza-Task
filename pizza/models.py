from django.db import models

# Create your models here.

class Pizza(models.Model):
    TYPE_CHOICES = [
        ('Regular','Regular'),
        ('Square','Square')
    ]

    type = models.CharField(max_length = 30,choices=TYPE_CHOICES,default=TYPE_CHOICES[0])
    size = models.CharField(max_length = 30)
    toppings = models.ManyToManyField('pizza.Topping',blank=True)

class Topping(models.Model):
    name = models.CharField(max_length = 30)
