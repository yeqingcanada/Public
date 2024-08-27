from django.db import transaction
from rest_framework import serializers

from .signals import order_created
from ..models import Cart, CartItem, Customer, Order, OrderItem
from ..cart.serializers import SimpleProductSerializer

"""
serializer 是为进行 object 与 json 的互相转换
render 接收 dict 返回 jason
serializer 中 save create validat 等自带方法都是为了进入数据库,定义 field 的方法都是为了从后端到前端展示数据,都是只读项,不会影响post或者patch,比如说cart item中的total_price。post的时候就看不到这条
"""

class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'unit_price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'items']

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart with the given ID was found.')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty.')
        return cart_id

    def save(self, **kwargs):
        """with transaction.atomic():意味着如果中途中断,会全部返回,不会只执行一半"""
        with transaction.atomic():
            cart_id=self.validated_data['cart_id']
            (customer,created) = Customer.objects.get_or_create(user_id=self.context['user_id'])
            """create an order"""
            order = Order.objects.create(customer=customer)

            cart_items = CartItem.objects\
                                    .select_related('product')\
                                    .filter(cart_id=cart_id)
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    unit_price=item.product.unit_price,
                    quantity=item.quantity
                ) for item in cart_items
            ]
            """create a bunch of order items"""
            OrderItem.objects.bulk_create(order_items)
            """delete the cart"""
            Cart.objects.filter(pk=cart_id).delete()
            """send_robust, 如果是普通的send,if one of the receivers fails and throws an exception, the other receivers are not notified"""
            """we need to pass the argument called sender, this is the class that is sending the signal. when we calling a handler, we need to supply the sender argument."""
            """self.__class__ this is a magic attribute that returns the class of the current isntance"""
            """optionally, we can supply additional data with our signal, in this case the order that was created, pass it ass a keyword argument"""
            """ now in store app, every time we create an order, we fire this signal. then we can to go core app, and recieve the signal"""
            order_created.send_robust(self.__class__, order=order)
        
            return order

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']