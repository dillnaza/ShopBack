from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=30)
    description=models.TextField()
    coint=models.IntegerField()
    is_acitive=models.BooleanField()


class Catrgories(models.Model):
    name=models.CharField(max_length=50)

