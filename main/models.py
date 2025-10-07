import uuid
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
    ('shoes', 'Shoes'),
    ('jersey', 'Jersey'),
    ('accessories', 'Accessories'),
    ('keychain', 'Key Chain'),
    ('bag', 'Bag'),
    ('ball', 'Ball'),
    ('gloves', 'Gloves'),
    ('hat', 'Hat'),
    ('watch', 'Watch'),
    ('scarf', 'Scarf'),
    ('socks', 'Socks'),
    ('water_bottle', 'Water Bottle'),
    ('poster', 'Poster'),
    ('magazine', 'Magazine'),
    ('sticker', 'Sticker'),
    ('others', 'Others'),
    ]
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0, message='Price cannot be negative.')])
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(validators=[MinValueValidator(0, message='Stock cannot be negative.')], default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    views = models.IntegerField(default=0) 

    def __str__(self):
        return self.name

    @property
    def is_hot(self):
        return self.views > 20

    def increment_views(self):
        self.views += 1
        self.save()
