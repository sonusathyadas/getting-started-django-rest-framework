from django.db import models

class CatalogItem(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    mfg_date = models.DateField(name="manufacturing_date")
    brand = models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)