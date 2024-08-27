from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.http import QueryDict
from rest_framework import serializers
from .models import Product, Collection, Review, Cart, CartItem
from decimal import Decimal

from .advanced_api.image.serializers import ProductImageSerializer


# more in django-rest-framework.org

"""
serializer 是为进行 object 与 json 的互相转换
render 接收 dict 返回 jason
serializer 中 save create validate 等自带方法都是为了进入数据库;定义 field 的方法都是为了从后端到前端展示数据,都是只读项,不会影响post或者patch,比如说cart item中的total_price。post的时候就看不到这条
"""


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

# 可以被写成serializers.ModelSerializer,不必每个field自己重新定义
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # method one：返回collection的id, 是数字
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all()
#     # )
#     # method two：product中的collection是以string形式表现的
#     # collection = serializers.StringRelatedField()
#     # method three: nested object
#     # collection = CollectionSerializer()
#     # method four: 加超链接
#     # view_name='collection-detail'： URL中：path('collections/<int:pk>', views.collection_detail, name='collection-detail')
#     collection =serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         # view_name is used for generate Hyperlink
#         view_name='collection-detail'
#     )

#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)


class ProductSerializer(serializers.ModelSerializer):
    # collection 可以被重写
    # collection =serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     # view_name is used for generate Hyperlink
    #     view_name='collection-detail'
    # )

    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection', 'images']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # """在serializer层面重写validation"""
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    # """所以validate方法返回一个ValidationError或者data(通过了validate)"""
    #         return serializers.ValidationError('Passwords do not match')
    #     return data

    # """在serializer层面重写save/create/update
    # def create()在base model serializer class中原本就有这个方法。
    # 当save方法在create a new product的时候, create() 方法会被执行。
    # 当save方法在update a existing product的时候, update() 方法会被执行。
    # 不论post还是put,save都被call,post的话会在save内部call create,put的话会在save内部call update
    # validated_data是一个dictionary, 两个星号是unpack这个字典"""
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

############################################# I am a beautiful dividing line #############################################
