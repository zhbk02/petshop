from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

