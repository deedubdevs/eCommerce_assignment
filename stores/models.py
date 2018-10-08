from django.db import models
from users.models import CustomUser


class Store(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop', default='<eCommerce>/static/icons/shop.png', blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class StoreItems(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
