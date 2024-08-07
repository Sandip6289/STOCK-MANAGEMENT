from django.urls import path
from . import views

from django.conf.urls.static import static
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('index', views.Index.as_view(), name='index'),
    path('show_product', views.ShowProduct.as_view(), name='show_product'),
    path('add_product',views.AddProduct.as_view(), name='add_product'),
    path('store_product_in_db',views.StoreProductInDB.as_view(), name='store_product_in_db'),
]
