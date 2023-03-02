from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
