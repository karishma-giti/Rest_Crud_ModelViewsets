from .models import Product
from .serializers import ProductSerializer
from rest_framework import mixins,viewsets
from rest_framework.response import Response

class ProductModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class UserViewSet(viewsets.GenericViewSet):
      def get_queryset(self):
            queryset = Product.objects.all()
            return queryset

      def get_object(self):
            queryset = self.get_queryset()
            obj = queryset.get(pk=self.kwargs['pk'])
            return obj

      def list(self, request):
            queryset = self.get_queryset()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)

      def retrieve(self, request, **kwargs):
            obj = self.get_object()
            serializer = ProductSerializer(obj)
            return Response(serializer.data)


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



          



