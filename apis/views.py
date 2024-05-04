from webapp.models import Customer, Product
from rest_framework import permissions, viewsets
from .serializers import CustomerSerializer, ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticate]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

