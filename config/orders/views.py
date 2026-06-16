from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from products.models import Product
from .models import Cart

# ADD To CART function
@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart_item = Cart.objects.filter(
        customer=request.user,
        product=product
    ).first()

    if cart_item:

        cart_item.quantity += 1

        cart_item.save()

    else:

        Cart.objects.create(
            customer=request.user,
            product=product,
            quantity=1
        )

    return redirect('cart')

# Cart view
@login_required
def cart(request):

    cart_items = Cart.objects.filter(
        customer=request.user
    )

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    return render(
        request,
        'orders/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )
