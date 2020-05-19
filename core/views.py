from django.shortcuts import render


def product(request):
    return render(request, 'core/product.html')


def dashboard(request):
    return render(request, 'core/dashboard.html')


def customer(request):
    return render(request, 'core/customer.html')
