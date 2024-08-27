from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Collection, Product
from ..serializers import ProductSerializer,CollectionSerializer
from rest_framework import status
from rest_framework.views import APIView

# --------------------------------Building RESTful APIs with Django REST Framework----------------------------------------

# 原始django自带的HttpResponse
# def product_list(request):
#     return HttpResponse('ok')

# rest_framework带的Response,会生成browserable api,页面效果不同,还有很多其他powerful的功能
# @api_view()
# def product_detail(request,id):
#     return Response(id)


# 如果不需要其他http方法,get是default的,不用特别声明
# @api_view()
# def product_list(request):
#     queryset = Product.objects.select_related('collection').all()
#     # context={'request': request} 这句话是为了,serializer里面有hyper link,需要context
#     serializer = ProductSerializer(queryset, many=True, context={'request': request})
#     return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        # method one:
        # """serializer.is_valid()这个方法被调用完成,就会生成一个validated_data, which is a dictionary"""
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('ok')
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # method two, 简化版
        serializer.is_valid(raise_exception=True)
        # """以下,post product,terminal会打印一个有序字典"""
        # print(serializer.validated_data)
        # 可以不用访问validated_data来save,因为django自带save会自动提取validated_data,进行存储
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# create a new product
# {
# "title":"a",
# "slug": "a",
# "unit_price":1,
# "collection":1,
# "inventory": 1
# }



# 以下只有get方法
# @api_view()
# def product_detail(request, id):
#     # method one:
#     # try:
#     #     product = Product.objects.get(pk=id)
#     #     serializer = ProductSerializer(product)
#     #     return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)

#     # method two:
#     product = get_object_or_404(Product,pk=id)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


@api_view(['GET', 'PUT','DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(
            products_count=Count('products')), pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
