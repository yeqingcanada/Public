from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>', views.product_detail),
    path('collections/', views.collection_list),
    # django 使用pk,获取url中s,use that to lookup a collection。这是为了productSerializer中hyperLink引用collection设置的
    path('collections/<int:pk>', views.collection_detail, name='collection-detail')
]
