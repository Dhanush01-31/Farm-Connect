from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'register/',
        register_view,
        name='register'
    ),

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'farmer-dashboard/',
        farmer_dashboard,
        name='farmer_dashboard'
    ),

    path(
        'customer-dashboard/',
        customer_dashboard,
        name='customer_dashboard'
    ),

    path(
    'dashboard/',
    dashboard,
    name='dashboard'
    ),

]