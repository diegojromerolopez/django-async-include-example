from django.db import models


class ShopList(models.Model):
    name = models.CharField(max_length=256)
    comments = models.TextField(null=True, default=None)
    created_at = models.DateTimeField('Creation date', auto_now_add=True)


class Item(models.Model):
    shop_list = models.ForeignKey(ShopList, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    units = models.PositiveIntegerField(default=1)
    comments = models.TextField(null=True,  default=None)
