from django.conf.urls import url
from . import views

app_name='product_page'

urlpatterns = [
    url('addlistproduct',views.add_list_product, name='addlistproduct'),
    url('updateproduct', views.update_product, name='updateproduct')
]