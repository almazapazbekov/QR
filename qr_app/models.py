from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    qr_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
