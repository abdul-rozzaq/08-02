from django.core import validators
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(validators=[validators.MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=128)
    rate = models.IntegerField(validators=[validators.MinValueValidator(1)])

    def __str__(self) -> str:
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=128)
    comment = models.TextField()
    date = models.DateField()
    price = models.IntegerField(validators=[validators.MinValueValidator(0)])
    klass = models.ForeignKey(Class, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
