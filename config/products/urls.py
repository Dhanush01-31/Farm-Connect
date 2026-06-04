from django.urls import path
from .views import *

urlpatterns = [

    path(
        'my-products/',
        product_list,
        name='product_list'
    ),

    path(
        'products/',
        products_page,
        name='products'
    ),

    path(
        'add-product/',
        add_product,
        name='add_product'
    ),

    path(
        'update-product/<int:pk>/',
        update_product,
        name='update_product'
    ),

    path(
        'delete-product/<int:pk>/',
        delete_product,
        name='delete_product'
    ),
]