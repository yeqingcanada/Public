from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

"""在auth/user/页面可以register新用户,但是只包含username,password,和email address。如果想重写djoser.serializers中的UserCreateSerializer,可以在core这个位置,写custom的UserCreateSerializer"""
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


"""其他改变,请查看djoser doc,serializers"""
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']