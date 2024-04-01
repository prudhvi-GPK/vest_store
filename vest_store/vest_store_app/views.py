from django.shortcuts import render,redirect

# Create your views here.from django.shortcuts import render
def home(request):
    return render(request, 'vest_store_app/home.html')

def about_page(request):
    return render(request, 'vest_store_app/about.html')

def cart_page(request):
    cart = request.session.get('cart', {})
    return render(request, 'vest_store_app/cart.html', {'cart': cart})




def add_to_cart(request, quantity, size):
    cart = request.session.get('cart', {})

    # Assuming each vest has a unique ID, you might need to adjust this based on your model
    vest_id = f'vest_{size}'

    if vest_id in cart:
        cart[vest_id] += quantity
    else:
        cart[vest_id] = quantity

    request.session['cart'] = cart
    request.session.modified = True

    print("Cart contents after adding:", request.session.get('cart', 'Cart is empty'))

    return redirect('cart_page')
