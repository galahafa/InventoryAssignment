from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=1024)

    class Meta:
        db_table = 'suppliers'


class Inventory(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        db_table = 'inventories'
