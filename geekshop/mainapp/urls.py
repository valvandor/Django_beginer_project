from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('products/', mainapp.products, name='product'),
    path('products/<slug:slug>/', mainapp.products_category, name='products_category'),
    path('contact/', mainapp.contact, name='contact'),
    path('', mainapp.index, name='index'),
]
