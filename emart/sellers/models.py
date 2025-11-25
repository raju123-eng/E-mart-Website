from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class SellerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200)
    about = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='store_banners/', blank=True, null=True)

    def __str__(self):
        return self.store_name
