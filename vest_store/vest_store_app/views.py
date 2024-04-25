from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserDetails
from .models import Vest



def home(request):
    # Retrieve all vest objects from the database
    vests = Vest.objects.all()
    return render(request, 'vest_store_app/home.html', {'vests': vests})

def about_page(request):
    return render(request, 'vest_store_app/about.html')

def cart_page(request):
    cart = request.session.get('cart', {})
    return render(request, 'vest_store_app/cart.html', {'cart': cart})




def add_to_cart(request, quantity, size):
    cart = request.session.get('cart', {})

    vest_id = f'{size}'

    if vest_id in cart:
        cart[vest_id] += quantity
    else:
        cart[vest_id] = quantity

    request.session['cart'] = cart
    request.session.modified = True

    print("Cart contents after adding:", request.session.get('cart', 'Cart is empty'))

    return redirect('cart_page')

def delete_from_cart(request, size):
    cart = request.session.get('cart', {})
    vest_id = f'{size}'
    print(vest_id)

    if vest_id in cart:
        del cart[vest_id]
        request.session['cart'] = cart
        request.session.modified = True

    print("Cart contents after deleting:", request.session.get('cart', 'Cart is empty'))

    return redirect('cart_page')

def checkout(request):
    # Your checkout logic goes here
    return render(request, 'vest_store_app/checkout.html')

def order_confirmation(request):
    # Your order confirmation logic goes here
    return render(request, 'vest_store_app/order_confirmation.html')
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

