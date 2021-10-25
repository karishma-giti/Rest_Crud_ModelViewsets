from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
