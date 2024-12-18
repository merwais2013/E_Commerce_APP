from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True, default="Germany")
    old_cart = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, created, instance, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)
    picture = models.ImageField(upload_to='upload/product/')
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    quantity = models.IntegerField(default=0)
    is_sale = models.BooleanField(default=False)
    discount_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class Order(models.Model):
    # Foreign key to the customer model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    # Foreign key to the product model
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    # Other fields
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField(default='', blank=False)
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.customer}"
