from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from products.models import Product
from sellers.models import SellerProfile

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending Payment'),
        ('paid','Paid'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    )
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(blank=True, null=True)

    def __str__(self): return f'Order {self.id} - {self.buyer}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)

    def __str__(self): return f'{self.product.title} x {self.quantity}'
