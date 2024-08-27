from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('carts', views.CartViewSet)



"""kwargs['cart_pk'],cart_pk中的cart,是从
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
中的lookup获取的"""
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + carts_router.urls
