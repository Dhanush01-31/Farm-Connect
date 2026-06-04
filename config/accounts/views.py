from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


# Home Page
def home(request):
    return render(request, 'home.html')


# Register View
def register_view(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            print("USER CREATED:", user.username)

            login(request, user)

            if user.role == 'farmer':
                return redirect('farmer_dashboard')

            return redirect('customer_dashboard')

        else:
            print("FORM ERRORS:")
            print(form.errors)

    else:
        form = UserRegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


# Login View
def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            if user.role == 'farmer':
                return redirect('farmer_dashboard')

            return redirect('customer_dashboard')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


# Logout View
def logout_view(request):

    logout(request)

    return redirect('login')


# Farmer Dashboard
@login_required(login_url='login')
def farmer_dashboard(request):

    if request.user.role != 'farmer':
        return redirect('customer_dashboard')

    return render(
        request,
        'accounts/farmer_dashboard.html'
    )


# Customer Dashboard
@login_required(login_url='login')
def customer_dashboard(request):

    if request.user.role != 'customer':
        return redirect('farmer_dashboard')

    return render(
        request,
        'accounts/customer_dashboard.html'
    )

@login_required
def dashboard(request):

    if request.user.role == 'farmer':
        return redirect('farmer_dashboard')

    return redirect('customer_dashboard')

