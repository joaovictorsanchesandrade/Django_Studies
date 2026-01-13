from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)