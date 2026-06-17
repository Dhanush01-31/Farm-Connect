from django.urls import path
from .views import *

urlpatterns = [

    path(
        'add-to-cart/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        cart,
        name='cart'
    ),

    path(
    'remove-from-cart/<int:cart_id>/',
    remove_from_cart,
    name='remove_from_cart'
    ),

    path(
    'increase-quantity/<int:cart_id>/',
    increase_quantity,
    name='increase_quantity'
    ),

    path(
        'decrease-quantity/<int:cart_id>/',
        decrease_quantity,
        name='decrease_quantity'
    ),

    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'order-success/',
        order_success,
        name='order_success'
    ),

    path(
        'my-orders/',
        my_orders,
        name='my_orders'
    ),
        path(
    'farmer-orders/',
    farmer_orders,
    name='farmer_orders'
),

path(
    'update-order-status/<int:order_id>/',
    update_order_status,
    name='update_order_status'
),
]