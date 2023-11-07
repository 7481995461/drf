from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list ->Queryset
    get -> Retrive -> Product Instane Detail View
    post -> Create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    
    '''
    

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'