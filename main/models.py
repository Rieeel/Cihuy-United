import uuid
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0, message='Price cannot be negative.')])
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
