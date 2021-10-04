from django.urls import re_path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^(?P<product_id>\d+)/$', mainapp.product_detail, name='product_detail'),
    re_path(r'^(?P<category_name>\w+)/$', mainapp.products, name='products_category'),
    re_path(r'^(?P<category_name>\w+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
]
