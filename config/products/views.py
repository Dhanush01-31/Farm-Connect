from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

# add product view
@login_required(login_url='login')
def add_product(request):

    if request.user.role != 'farmer':
        return redirect('dashboard')

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.farmer = request.user

            product.save()

            return redirect('product_list')

    else:
        form = ProductForm()

    return render(
        request,
        'products/add_product.html',
        {'form': form}
    )


# product list view
@login_required(login_url='login')
def product_list(request):

    products = Product.objects.filter(
        farmer=request.user
    )

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )

# Update product view
@login_required(login_url='login')
def update_product(request, pk):

    product = get_object_or_404(
        Product,
        id=pk,
        farmer=request.user
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect('product_list')

    else:
        form = ProductForm(
            instance=product
        )

    return render(
        request,
        'products/update_product.html',
        {'form': form}
    )


# delete product view
@login_required(login_url='login')
def delete_product(request, pk):

    product = get_object_or_404(
        Product,
        id=pk,
        farmer=request.user
    )

    product.delete()

    return redirect('product_list')


def products_page(request):

    products = Product.objects.all()

    search = request.GET.get('search')

    if search:
        products = products.filter(
            name__icontains=search
        )

    return render(
        request,
        'products/products.html',
        {
            'products': products
        }
    )