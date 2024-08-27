from django.contrib import admin, messages
from django.http import HttpRequest
from . import models
from django.urls import reverse
# format_html是为了生成generate HTML link
from django.utils.html import format_html, urlencode
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet


# is_staffing means this is an admin user for this website
# 如果是admin,则可以利用termianl重置password
# ./manage.py changepassword ye@miebach.com

# more in google 'Django ModelAdmin', 'Model Admin options'
# admin中填写的form的validate,都是在model中添加的。blank=True,MinValueValidator(1)......

# 自定义filter：parameter_name被用于query string. on the admin page, 'By inventory(parameter_name): All/Low(options)'
class InventoryFilter(admin.SimpleListFilter):
    # title 使用在filter的‘By TITLE’
    # parameter_name 用在生成的url处
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''

# method one:


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # # fields 这部分是用来定义form中(用以修改),哪些属性可以被显示
    # fields = ['title']
    # # 除了title都显示
    # exclude = ['promotions']
    # # form中不可以修改,只读
    # readonly_fields = ['title']
    #############################################################
    # 外键会有下拉菜单，在下拉菜单中添加search功能：
    # 在collection 中就需要添加search_fields因为product中有关于她的autocomplete_fields
    autocomplete_fields = ['collection']
    # 写了title，slug会自动title-title: prepopulated_fields = { 'slug': ['title'] }
    # 碰slug之前,slug的值会根据title以及unit_price的输入,自动生成
    prepopulated_fields = {
        'slug': ['title', 'unit_price']
    }
    actions = ['clear_inventory']
    inlines = [ProductImageInline]
    # 新填一个column根据inventory计算，inventory_status
    # 想要collection中的特定attribute，collection中的title属性
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    # 如果不加这个行collection_title会造成过多query
    # 加list_select_related这句，就可以避免因为要关联collection而多出来的10条（collection有10条数据）query
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    search_fields = ['title']

    # 如果collection中不想看string presentation,想看某个具体的field。不能用collection__field
    def collection_title(self, product):
        return product.collection.title

    # 加最上面这个行@,是因为inventory_status只有ok和low,不方便排序
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    # 清空选中的product的inventory
    # custom action, action是admin页面上的操作,例如可以一次性清空一个product的库存inventory
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset: QuerySet):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.ERROR
        )

    """这步是为了将static中的css应用于product admin"""
    """ in css we have the concept of meida type
            screen: only apply to screen
            print: the styles will only be applied when printing a page"""
    class Media:
        css = {
            'all': ['store/styles.css']
        }

# method two:
# admin.site.register(models.Collection)
# admin.site.register(models.Product, ProductAdmin)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'membership']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    """ordering可以直接利用user外键, list_display不可以user__first_name。所以models中才需要加def first_name"""
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

# 在添加order的时候，想要一起添加order item：最少填一个最多填10个，extra为0不必显示过多的
# TabularInline 显示为一列列的,表格感
# StackedInline 显示为一行行的,每个新建Order Item,会显示为单独的form


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    # 意味着不会显示多余的行,需要按添加Order Item才会有多一行显示,用于新建Order Item
    extra = 0
    model = models.OrderItem
    min_num = 1
    max_num = 10

# 写在第一个位置的field(以下是id),会自带一个link,link到这个object(order)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    # OrderItemInline是指在新建order form中,会有一个嵌套的form,用于新建orderItem
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    # products_count是原本没有的attribute,需要在get_queryset的时候添加
    # override the base query set use a rendering a list page. let's say we want to add a new column to show the number of products in each collection
    list_display = ['title', 'products_count']
    # search_fields 是为了product form中,collection下拉菜单中可以使用search,而不用全部显示(那就太长了)
    search_fields = ['title']

    # reverse('admin:app_model_page'),不想hard code url,希望django to give us the url of this page
    # 因为没有products_count这个属性，所以需要override
    # reverse 的规则： reverse('admin:app_model_page')
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        # url=()括号是用来让包裹的内容换行的
        # product 那页就是page changelist
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)

    # so this is where I am going to override the query set on this page and annotate our collections with a number of their products. so every model admin has a method called get query set, which we can override
    # 修改default的get_queryset,以便得到products_count
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
