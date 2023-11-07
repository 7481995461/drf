from django.http import JsonResponse
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializer
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)


@api_view(['POST'])
def api_home_post(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)
    return Response({"Invalid":"Not good data"},status=400)