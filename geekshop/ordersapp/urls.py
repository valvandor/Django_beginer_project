import ordersapp.views as ordersapp
from django.urls import re_path

app_name = "ordersapp"

urlpatterns = [
   re_path(r'^$', ordersapp.OrderList.as_view(), name='orders_list'),
]