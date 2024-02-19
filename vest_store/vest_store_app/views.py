from django.shortcuts import render

# Create your views here.from django.shortcuts import render
def home(request):
    return render(request, 'vest_store_app/home.html')

def about_page(request):
    return render(request, 'vest_store_app/about.html')

def cart_page(request):
    return render(request, 'vest_store_app/cart.html')

