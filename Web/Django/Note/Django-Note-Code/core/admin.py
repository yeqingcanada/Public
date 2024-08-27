from store.models import Product
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin, ProductImageInline
from tags.models import TaggedItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

"""
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
重写这个admin。
在admin page上看到user这个model
"""


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # pass
    """点开BaseUserAdmin查看,可见到add_fieldsets,这些是在registering a new user的时候可以看到的field"""
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )


# Extending Pluggable Apps：store admin 中，一个app（product） dependent在另一个（tag）上，这样就不能独立的运行和发布了，可以利用store_custom分开两者。效果就是，如果installed app中没有store_custom，product也可以独立运行，只不过admin page中product添加页面没有tag部分
# 这个模块的作用是,使得store不必依附于tag,store的admin中product想要,新建product的时候,同时新建几个tag(就是product admin中form)
# 这里的unregister和从新register可以做到这个
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    """ProductImageInline如果不加这行,product中的inlines就会覆盖这里的inlines"""
    inlines = [TagInline, ProductImageInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
