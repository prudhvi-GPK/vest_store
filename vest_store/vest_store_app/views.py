from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserDetails
from .models import Vest
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def email_notification(request):
    return render(request, 'vest_store_app/email_notification.html')

def send_email(request):
    subject = 'Test Email Notification'
    message = 'This is a test email notification.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['iylamsriramteja@gmail.com']

    send_mail(subject, message, email_from, recipient_list)
    
    return render(request, 'vest_store_app/email_notification.html')



def home(request):
    # Retrieve all vest objects from the database
    vests = Vest.objects.all()
    for vest in vests:
        if vest.stock < 5:
            # Compose your email message
            subject = 'Low Stock Notification'
            message = f'The stock for {vest.size} is running low. we are left with {vest.stock}Please replenish.'
            recipient_list = ['iylamsriramteja@gmail.com']
            email_from = settings.EMAIL_HOST_USER

            # Send the email
            send_mail(subject, message, ' email_from', recipient_list)
            
            # Email sent, break the loop
            break

    # Render your home template
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

