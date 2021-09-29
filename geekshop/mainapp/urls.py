from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('<int:product_id>/', mainapp.product_detail, name='product_detail'),
    path('', mainapp.products, name='products_main'),
    path('<slug:category_name>/', mainapp.products, name='products_category'),
    path('<slug:category_name>/page/<int:page>/', mainapp.products, name='page'),
]
