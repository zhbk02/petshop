from rest_framework import serializers

from .models import Product, Category
from review.models import Review

from django.contrib.auth.models import User
from review.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance: Product):

        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep["author"] = User.objects.get(user=request.user, product=instance)
        rep["text"] = ReviewSerializer(Review.objects.get(user=request.user, product=instance)).data
        rep["rating"] = Review.objects.get(user=request.user, product=instance)

        return rep


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
