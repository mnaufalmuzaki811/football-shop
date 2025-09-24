from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, default="new")
    is_featured = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    @property
    def final_price(self):
        return self.price * (1 - self.discount / 100)
    
    @property
    def is_available(self):
        return self.stock > 0

    