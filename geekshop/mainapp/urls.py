from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products_main, name='products_main'),
    path('<slug:category_name>/', mainapp.products_category, name='products_category'),
    path('<int:product_id>', mainapp.product_detail, name='product_detail'),
]
