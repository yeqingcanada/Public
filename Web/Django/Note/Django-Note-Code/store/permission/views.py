from urllib import response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from store.permission.permissions import FullDjangoModelPermissions, ViewCustomerHistoryPermission
from ..models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    """这里返回的是class。这里是一个list, any of them fails, the client won't access"""
    """只有admin可以做关于customer的调整,其他人只能access me,查看自己的profile"""
    permission_classes = [IsAdminUser]

    """Applying Model Permissions"""
    """permission_classes django model permissions, the uer has to be authenticated, and they should have the relevant model permissions"""
    """DjangoModelPermissions中有: 'POST': ['%(app_label)s.add_%(model_name)s'], 这部分add_%(model_name)对应着table permissions 中的code name add_customers"""
    """有这行permission_classes = [DjangoModelPermissions]的效果是,属于customer group的users,可以post等"""
    """DjangoModelPermissionsOrAnonReadOnly 与 DjangoModelPermissions 几乎一模一样,反正我没看处区别来"""
    # permission_classes = [DjangoModelPermissions]
    """custome permissions class"""
    # permission_classes = [FullDjangoModelPermissions]

    """以下这段,意味着未匿名用户只可以get不可以post等其他方法"""
    # def get_permissions(self):
    #     if self.request.method =='GET':
    #         """这里返回的是object"""
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    """detail=False意味着this action is available on the list view; true is on the detail view"""
    """action很特别,可以直接加载url,不同于其他view set中的方法。其他方法都是重写,get query set,delete,get serializer context"""
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """get_or_create 返回一个tuple,包含两个元素,第一个是这个object,第二个是告诉你是true created还是false get"""
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            """me这个action/api,是因为,需要从request中获取user id,如果从前端获取了user id,并且直接访问customer/user_id,就可以不必写这么一大堆"""
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    """this is for a particular customer, detail=True意味着这个url是/store/customers/pk/history/"""
    """跟model中的permission没关系,view_history或者cancel_order,都只是代号,四步走,第一,在model中添加cancel_order这步不重要,只是个代号。cancel_order这个必须在model中被定义。第二user选择cancel_order(最好不要user直接选择,最好是user属于group,group有permissions,拥有permission可以visit),第三,request.user.has_perm('store.cancel_order'),第四permission_classes=[ViewCustomerHistoryPermission]"""
    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('OK')
