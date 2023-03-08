from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    product = models.ForeignKey(Category, on_delete=models.CASCADE)
    bought = models.BooleanField()
    data = models.DateField()

    def __str__(self):
        return self.name
