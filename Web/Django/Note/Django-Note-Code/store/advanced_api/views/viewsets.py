from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from store.advanced_api.views.pagination import DefaultPagination
from store.permission.permissions import IsAdminOrReadOnly

from ...models import Product, Collection, OrderItem, Review
from ...serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from .filters import ProductFilter

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
"""一般的ModelViewSet"""

# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
"""希望在url中/store/products/?colletion_id=1,可以返回filter过的products set"""
"""Django uses the query set ttribute to figure out the base name. 因为重写了 get_queryset, django cannot find what the base name should be called. 因为我们移除了query_set, 所以django不能认出 base name. 所以应该在products URL这里添加 basename: router.register('products', viewsets.ProductViewSet, basename='products'). 便于django 根据这个属性, generate URL"""

# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         """以下,当url中没有collection部分的？filter参数的时候,会报错MultiValueDictKeyError
#         query_params is a dictionary, we expect a the dic always has a key 'collection_id', but sometimes it hasn't"""
#         # collection_id = self.request.query_params['collection_id']
#         """以下,也可以添加一个default的collection. 相比于之前，利用get方法，如果没有，会返回none，就不报错了"""
#         collection_id = self.request.query_params.get('collection_id')
#         if collection_id is not None:
#             queryset = queryset.filter(collection_id=collection_id)
#         return queryset

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
"""
django_filters
除了 collection, 我还想filter其他属性, 可以写一个generic的filter, 安装一个third party library
使用django_filters来制作generic filter,可以规定一个list,设置多个filter对象。可视化api中会出现一个filter button,帮助filter collection
去掉get_queryset 方法, 写：
filter_backends = [DjangoFilterBackend]
filterset_fields = ['collection_id']
"""

""" searching sorting """


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     """SearchFilter: 使用django_filters,制作有search功能的api。url是store/products/?search=coffee+10oz,意味着搜索title,description或者collection__title中包含both coffee and 10oz的条目"""
#     """OrderingFilter: 升序store/products/?ordering=unit_price&search=coffee, 降序store/products/?ordering=-unit_price&search=coffee。也可以同时多个排序,store/products/?ordering=-unit_price, last_update, 这个url意味着unit_price降序,last_update升序"""
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     """这里是自制的filter,因为unit price如果是filter等于一个值,未免奇怪。应该是一个区间,不应该是一个值"""
#     # filterset_fields = ['collection_id', 'unit_price']
#     filterset_class = ProductFilter
#     search_fields = ['title', 'description', 'collection__title']
#     ordering_fields = ['unit_price', 'last_update']

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)


# --------------------------------------------I am a beautiful dividing line------------------------------------------------
"""Pagination API, 可以分页的访问, 返回部分data"""

""" 一
只有ProductViewSet中有分页：
from rest_framework.pagination import PageNumberPagination

pagination_class = PageNumberPagination

settings.py:
REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}

每次返回10条，外加一个next and previous
"next": "http://127.0.0.1:8000/store/products/?page=3"
"previous": "http://127.0.0.1:8000/store/products/"
"""

""" 二
希望全部view set都有分页：
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
delete 这句code： pagination_class = PageNumberPagination in ProductViewSet
"""

""" 三
使用limit offset抵消 pagination. 下一页，我们会get 10个products，并且skip 10个products. 
"next": "http://127.0.0.1:8000/store/products/?limit=10&offset=10"
ProductViewSet 中啥也不用写，不用写pagination_class。只需要改settings中DEFAULT_PAGINATION_CLASS

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
"""

""" 四
个性化paginate，重写PageNumberPagination
只要 settings中没有DEFAULT_PAGINATION_CLASS 但是有PAGE_SIZE，就会报错： you have specified a default PAGE_SIZE pagination rest_framework setting, without specifying also a DEFAULT_PAGINATION_CLASS。实际上‘一’也有这个warning，可以不处理。
设置了default page size,却没有设置DEFAULT_PAGINATION_CLASS会报warning(),两种办法,其一,suppress warning 不处理。其二,建立一个custom的pagination class,重写PageNumberPagination for product view

pagination_class = DefaultPagination
"""


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    """需要去settings中REST_FRAMEWORK设置page size"""
    # pagination_class = PageNumberPagination
    """个性化,重写PageNumberPagination"""
    pagination_class = DefaultPagination
    search_fields = ['title', 'description', 'collection__title']
    ordering_fields = ['unit_price', 'last_update']
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    """destroy是在具体一个product页面delete。如果使用delete方法,在product list page也会错误的出现一个delete button,但是这个button不work,因为没有PK传入。在one project中也有一个delete button,这个button可以正常delete"""

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

    # def delete(self,request, pk):
    #     product = get_object_or_404(Product,pk=pk)
    #     if product.orderitems.count() > 0:
    #         return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------------------I am a beautiful dividing line------------------------------------------------

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    """custome的permission,admin可以post等,其他人只能read"""
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
