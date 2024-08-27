from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


"""没有以下这个permission class,匿名用户可以访问customer model,添加了这个permission后,必须属于customer group才能get"""
class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    """以下是改写DjangoModelPermissions中的__init__方法"""
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


"""想要以下生效,需要去admin users中,给一个user view history的权限"""
class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        """the user object has a method called has_perm, here we pass the code name for the permission"""
        return request.user.has_perm('store.view_history')
        # return request.user.has_perm('store.cancel_order')
        