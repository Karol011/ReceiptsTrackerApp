from django.db import models

# Create your models here.

class Receipt(models.Model):
    shop_name = models.CharField(max_length=50)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shop_name + ":"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE, null = True, default='None')


    def __str__(self):
        return self.name + ": " + str(self.price) + ": " + str(self.receipt)




