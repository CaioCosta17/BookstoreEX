from django.db import models
from django.contrib.auth.models import User
from product.models.product import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

    def __unicode__(self):
        return f'Order {self.id} by {self.user.username}'