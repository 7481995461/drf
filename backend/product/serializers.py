from rest_framework import serializers
from .models import Product
from . import validators
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )

    title = serializers.CharField(read_only=True)


 
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only = True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    body =serializers.CharField(source = 'content')
    class Meta:
        model = Product
        fields = ['owner',
                  'id',
                  'title',
                  'body', 
                  'price', 
                  'sale_price',
                  'public',
                  'path',
                  'endpoints'
                  ]  
  
    def get_Update_URL(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.id}, request=request)