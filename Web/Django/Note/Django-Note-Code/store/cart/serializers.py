from rest_framework import serializers

from ..models import Cart, CartItem, Product


"""
serializer 是为进行 object 与 json 的互相转换
render 接收 dict 返回 jason
serializer 中 save create validat 等自带方法都是为了进入数据库,定义 field 的方法都是为了从后端到前端展示数据,都是只读项,不会影响post或者patch,比如说cart item中的total_price。post的时候就看不到这条
"""


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']


"""CartItemSerializer 不写cart这个field,因为cartitem是在cart下一个级别的,会自带cart id
ProductSerializer() 要带括号"""


class CartItemSerializer(serializers.ModelSerializer):
    """read_only=True是为了,post的时候,不必post整个product,只需要product id,而非一整个object。但是这么一整,post的时候就干脆看不到product的任何痕迹了。所以想添加一项product_id实际上这个product id只有在post的时候有用,这么一整,一来有所重复,二来,当update的时候我们也不想send product_id,所以product_id也需要是read only的,这就很糟心。所以,需要写一个新的serializer"""
    # product = SimpleProductSerializer(read_only=True)
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')

    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.unit_price * cart_item.quantity

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


"""read_only 意味着user不能编辑id,id在post的时候自动生成"""
"""on_delete=models.CASCADE,当一个cart被删除的时候,这个cart中的所有cart item会自动被删除,不必再serializer中特意写这段逻辑"""


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')

    def get_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']


"""可以被写成serializers.ModelSerializer,不必每个field自己重新定义。我写错了,写成了serializers.Serializer,post的时候,就一个field也看不到,因为没有定义过任何field"""


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    """以下是为了处理,post的时候,product id不存在的情况。这个方法的名字是django convention,意思是validate product id。这个方法返回ValidationError或者value"""
    """不必写validate_quantity,因为这个attribute是直接从model来的,quantity规定为正整数,直接就有这个validation"""

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                'No product with the given ID was found.')
        return value

    """定义save方法,有些复杂,因为如果cart中已经有一个product了,添加相同的product,不想添加一个新的cart item,而是想update这个product"""
    """serializer.is_valid()这个方法被调用完成,就会生成一个validated_data, which is a dictionary。在model view set中,.is_valid()已经被默认调用过了,所以这里可以直接访问validated_data"""

    def save(self, **kwargs):
        """cart id 不在request中,在url中,在serializer中,我们不能访问url的parameter。所以需要在view中,取得url parameter,使用一个context object传参"""
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        """如果没有CartItem.objects.get(cart_id=cart_id, product_id=product_id)这样的cart item会抛出一个exception"""
        """shift + ctrl + o vscode命令@寻找函数,类...symbols defined in this module"""
        try:
            cart_item = CartItem.objects.get(
                cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            """以下这行,是查看了save的原始写法,需要按照其方法重写,需要定义一个instance,返回这个instance"""
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data)

        """self.instance 是一个object"""
        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['quantity']
