from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from shop.models import Product

class ShippingAddress(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  shipping_full_name = models.CharField(max_length=300)
  shipping_email = models.CharField(max_length=300)
  shipping_phone = models.CharField(max_length=25, blank=True, null=True)
  shipping_address1 = models.CharField(max_length=200, null=True, blank=True)
  shipping_address2 = models.CharField(max_length=200, null=True, blank=True)
  shipping_city = models.CharField(max_length=50, null=True, blank=True)
  shipping_state = models.CharField(max_length=50, null=True, blank=True)
  shipping_zipcode = models.CharField(max_length=50, null=True, blank=True)
  shipping_country = models.CharField(max_length=50, null=True, blank=True, default="Germany")

  class Meta:
    verbose_name_plural = 'Shipping Address'

  def __str__(self) -> str:
    return f'Shipping address from' + self.full_name

def create_shipping(sender, created, instance, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping, sender=User)


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  full_name=  models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  shipping_address = models.TextField(max_length=15000)
  amount_paid = models.DecimalField(default=0, max_digits=10, decimal_places=2)
  date_ordered = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'Order - {self.id}'

class OrderItem(models.Model):
  order = models.ForeignKey(Order, models.CASCADE, null=True)
  products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  quantity =  models.PositiveBigIntegerField(default=0,)
  price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

  def __str__(self) -> str:
    return f'Order Item - {self.id}'