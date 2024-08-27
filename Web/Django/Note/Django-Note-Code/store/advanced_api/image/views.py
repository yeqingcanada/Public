from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from ...models import ProductImage
from .serializers import ProductImageSerializer


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self):
        """这里使用的product_pk,原因是,/products/1(product_pk)/images/1(pk),url包含两个参数,第一个是product_pk,第二个是pk"""
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])