from django.db import models

# Create your models here.
class Item(models.Model):
    item_code = models.CharField(max_length=64)
    item_name = models.CharField(max_length=128)

    def __str__(self):
        return self.item_code + ' ' + self.item_name
