from django.shortcuts import render

# Create your views here.from django.shortcuts import render

def about_page(request):
    return render(request, 'vest_store_app/about.html')

def cart_page(request):
    return render(request, 'vest_store_app/cart.html')

