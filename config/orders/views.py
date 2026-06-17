from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, Order, OrderItem

# ADD To CART function
@login_required(login_url='login')
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
@login_required(login_url='login')
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

# remove cart item
@login_required(login_url='login')
def remove_from_cart(request, cart_id):

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        customer=request.user
    )

    cart_item.delete()

    return redirect('cart')

# Increase quantity of cart item
@login_required(login_url='login')
def increase_quantity(request, cart_id):

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        customer=request.user
    )

    cart_item.quantity += 1

    cart_item.save()

    return redirect('cart')

# Decrease quantity of cart item
@login_required(login_url='login')
def decrease_quantity(request, cart_id):

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        customer=request.user
    )

    if cart_item.quantity > 1:

        cart_item.quantity -= 1

        cart_item.save()

    else:

        cart_item.delete()

    return redirect('cart')

# checkout view
@login_required(login_url='login')
def checkout(request):

    cart_items = Cart.objects.filter(
        customer=request.user
    )

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    if request.method == 'POST':

        full_name = request.POST.get(
            'full_name'
        )

        phone = request.POST.get(
            'phone'
        )

        address = request.POST.get(
            'address'
        )

        order = Order.objects.create(

            customer=request.user,

            full_name=full_name,

            phone=phone,

            address=address,

            total_amount=total
        )

        for item in cart_items:

            OrderItem.objects.create(

                order=order,

                product=item.product,

                quantity=item.quantity,

                price=item.product.price
            )

        cart_items.delete()

        return redirect(
            'order_success'
        )

    return render(
        request,
        'orders/checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )

# order success view
@login_required(login_url='login')
def order_success(request):

    return render(
        request,
        'orders/order_success.html'
    )

# order history view
@login_required(login_url='login')
def my_orders(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders
        }
    )

# farmer order history view
@login_required(login_url='login')
def farmer_orders(request):

    if request.user.role != 'farmer':
        return redirect('dashboard')

    order_items = OrderItem.objects.filter(
        product__farmer=request.user
    ).select_related(
        'order',
        'product'
    )

    return render(
        request,
        'orders/farmer_orders.html',
        {
            'order_items': order_items
        }
    )

# update order status view
@login_required(login_url='login')
def update_order_status(
    request,
    order_id
):

    if request.user.role != 'farmer':
        return redirect('dashboard')

    order = get_object_or_404(
        Order,
        id=order_id
    )

    if request.method == 'POST':

        order.status = request.POST.get(
            'status'
        )

        order.save()

        return redirect(
            'farmer_orders'
        )

    return render(
        request,
        'orders/update_order_status.html',
        {
            'order': order
        }
    )

# 