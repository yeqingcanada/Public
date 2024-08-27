
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import Customer, Order
from .serializers import OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer




class OrderViewSet(ModelViewSet):
    # queryset = Order.objects.prefetch_related('items__product').all()
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()

        """这是为了获取customer_id,因为request中只包含user id"""
        """以下这句有个隐藏issue,如果customer表中,没有这个user,就会报错,这是因为使用get方法的隐藏issue。所以换成更下面一行"""
        # customer_id = Customer.objects.only(
        #     'id').get(user_id=user.id)

        """如果没有这个customer中没有这个user,就会新建一个customer"""
        """有了signal后,也不用这样写了,因为只要新建user就会直接新建一个customer,不会出现customer空缺error"""
        # (customer_id, created) = Customer.objects.only(
        #     'id').get_or_create(user_id=user.id)
        # return Order.objects.filter(customer_id=customer_id)
        customer_id = Customer.objects.only('id').get(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)

    """以下这句不用写,因为它只在使用create model mixin that we inherit in this class"""
    # def get_serializer_context(self):
    #     return {'user_id': self.request.user.id}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer


    """第一,到/store/carts/,post。第二,到/store/carts/8d195f36-77ca-4f39-92e8-866183e727b8/items/,post。第三到/store/orders/, post"""
    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data,
            context={'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        """serializer.save()返回一个order object,利用这个order新建一个serializer"""
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]