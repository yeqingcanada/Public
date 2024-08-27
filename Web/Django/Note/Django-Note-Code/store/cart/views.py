from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from ..models import Cart,CartItem
from .serializers import CartSerializer,  CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer


"""
CreateModelMixin---post
ListModelMixin---get all
RetrieveModelMixin---get one
UpdateModelMixin---put
DestroyModelMixin---delete
"""

"""PUT entire, PATCH part attribute"""

class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    """添加以上这行,是为了防止有put方法。如果有put方法,可视化api的input form中就会有entire attribute。没有put,就会按照UpdateCartItemSerializer中的field,只有quantity一个field。不必专门写一个delete的serializier,因为再delete一个cart item的时候,没有什么特别要做的事情"""
    
    """添加了add cart item serializer后,就不能hard code serializer_class = CartItemSerializer了。需要分情况讨论"""
    # serializer_class = CartItemSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    """cart_pk中的cart,是从
    carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
    中的lookup获取的"""
    def get_queryset(self):
        return CartItem.objects \
                .filter(cart_id=self.kwargs['cart_pk']) \
                .select_related('product')
