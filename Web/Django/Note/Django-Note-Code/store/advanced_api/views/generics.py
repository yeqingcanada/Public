from ast import Delete
import collections
from rest_framework.response import Response
from ...models import Product, Collection
from ...serializers import ProductSerializer, CollectionSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models.aggregates import Count
from rest_framework.viewsets import ModelViewSet

"""
def view ---> 
class view APIView(不需要多个if else, 只需要get/post) ---> 
ListCreateAPIView / RetrieveUpdateDestroyAPIView (只需要queryset & serializer_class) ---> 
ModelViewSet(将ProductList ProductDetail 合并)
"""


# more info for mixins in, django-rest-framework.org--->api guide--->generic views
# CreateModelMixin---post
# ListModelMixin---get all
# RetrieveModelMixin---get one
# UpdateModelMixin---put
# DestroyModelMixin---delete


# 1-method one:
# 改写以下内容
# @api_view(['GET', 'POST'])
# def product_list(request):
# 以上对应内容, 其他都跟def view 一样，但是不需要那么多 if else
# class ProductList(APIView):
#     def get(self, request):
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# 1-method two:
# ListCreateAPIView 可以替换APIView,需要重写两个方法,get_queryset & get_serializer_class
# 这个叫做generics view,可以自动生成input form,不用自己new json
class ProductList(ListCreateAPIView):
    # 2-method-1:
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()

    # def get_serializer_class(self):
    #     return ProductSerializer()

    # 以下方法是这个ProductList特别要处理的,因为APIView(method one)中,serializer需要context
    # def get_serializer_context(self):
    #     return {'request': self.request}

    # # 2-method-2:
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    # context={'request': request} 这句话是为了,serializer里面有hyper link,需要context
    def get_serializer_context(self):
        return {'request': self.request}

# 3-方法一
# class ProductDetail(APIView):
#     def get(self, request, id):
#         product = get_object_or_404(Product,pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     def put(self,request, id):
#         product = get_object_or_404(Product,pk=id)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request, id):
#         product = get_object_or_404(Product,pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 3-方法二


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # way 01
    # url中传递的是id,但是django默认pk。可以利用look_field告诉django,这次要看的是id
    # way 02,也可以类似collection,把url中的id,改为pk
    # look_field = 'id'

    # get和put中,没啥特别的,不用改写。
    # delete中有个判断,需要重写delete方法
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer


class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(
        products_count=Count('products'))
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(
            Collection.objects.annotate(
                products_count=Count('products')), pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
