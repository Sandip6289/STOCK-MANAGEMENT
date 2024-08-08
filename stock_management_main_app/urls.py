from django.urls import path
from . import views

from django.conf.urls.static import static
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('index', views.Index.as_view(), name='index'),
    path('show_product', views.ShowProduct.as_view(), name='show_product'),
    path('add_product',views.AddProduct.as_view(), name='add_product'),
    path('store_product_in_db',views.StoreProductInDB.as_view(), name='store_product_in_db'),
    path('store_category_in_db',views.StoreCategoryInDB.as_view(), name='store_category_in_db'),
    path('store_sub_category_in_db',views.StoreSubCategoryInDB.as_view(), name='store_sub_category_in_db'),
    
    path('add_category',views.AddCategory.as_view(), name='add_category'),
    path('add_sub_category',views.AddSubCategory.as_view(), name='add_sub_category'),
]
