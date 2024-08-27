from django.urls import path, include
# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from pprint import pprint

from .views import generics
from .views import viewsets
from .image import views

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
# generics ---> APIView / ListCreateAPIView / RetrieveUpdateDestroyAPIView
# urlpatterns = [
#     path('products/', generics.ProductList.as_view()),
#     path('products/<int:pk>', generics.ProductDetail.as_view()),
#     path('collections/', generics.CollectionList.as_view()),
#     path('collections/<int:pk>', generics.CollectionDetail.as_view(), name='collection-detail')
# ]

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
# router=SimpleRouter()
# router.register('products', viewsets.ProductViewSet)
# router.register('collections', viewsets.CollectionViewSet)

# # pprint(router.urls)
# # [<URLPattern '^products//$' [name='product-list']>,
# #  <URLPattern '^products//(?P<pk>[^/.]+)/$' [name='product-detail']>,
# #  <URLPattern '^collections//$' [name='collection-list']>,
# #  <URLPattern '^collections//(?P<pk>[^/.]+)/$' [name='collection-detail']>]

# # 方法一：
# # urlpatterns = router.urls

# # 方法二：
# urlpatterns = [
#     path('', include(router.urls)),
# ]

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
# # 利用default router,可以在可视化api界面上看到每个api的url link
# # 另一个多出来的功能是,如果输入http://127.0.0.1:8000/store/products.json, 可以看到所有products的json数据
# router=DefaultRouter()
# router.register('products', viewsets.ProductViewSet)
# router.register('collections', viewsets.CollectionViewSet)

# urlpatterns = router.urls

# --------------------------------------------I am a beautiful dividing line------------------------------------------------
# /domain/{domain_pk}/nameservers/{pk}
# router.register(r'domains', DomainViewSet)
# domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
# domains_router.register(r'nameservers', NameserverViewSet, basename='domain-nameservers')
# 第三行中的三个参数：
# router：parent router
# r'domains'：router.register(r'domains', DomainViewSet)中的r'domains'
# lookup='domain'：/domain/{domain_pk}/nameservers/{pk}中的{domain_pk}
# 第四行中的basename：用以产生url,会产生两个：domain-nameservers-list,domain-nameservers-detail


router = routers.DefaultRouter()
router.register('products', viewsets.ProductViewSet, basename='products')
router.register('collections', viewsets.CollectionViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register(
    'reviews', viewsets.ReviewViewSet, basename='product-reviews')
products_router.register(
    'images', views.ProductImageViewSet, basename='product-images')

# 方法一：
# urlpatterns = router.urls + products_router.urls

# 方法二：
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
]
