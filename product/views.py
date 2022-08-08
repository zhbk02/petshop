from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Product, Category

from review.serializers import ReviewSerializer
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination



# Create your views here.


class ProductViewSet(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'view.html'
    queryset = Product.objects.all()

    def get(self, request):
        queryset = Product.objects.all()

        return render(request, template_name='view.html', context={'products': queryset})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
