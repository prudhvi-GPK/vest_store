from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserDetails


def home(request):
    return render(request, 'vest_store_app/home.html')

def about_page(request):
    return render(request, 'vest_store_app/about.html')

def cart_page(request):
    cart = request.session.get('cart', {})
    return render(request, 'vest_store_app/cart.html', {'cart': cart})




def add_to_cart(request, quantity, size):
    cart = request.session.get('cart', {})

    vest_id = f'vest_{size}'

    if vest_id in cart:
        cart[vest_id] += quantity
    else:
        cart[vest_id] = quantity

    request.session['cart'] = cart
    request.session.modified = True

    print("Cart contents after adding:", request.session.get('cart', 'Cart is empty'))

    return redirect('cart_page')

def store_user_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        # Create a new instance of UserDetails model and save to the database
        user_details = UserDetails.objects.create(name=name, phone=phone, email=email)
        user_details.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})