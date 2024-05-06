from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import UserDetails
from .models import Vest
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def email_notification(request):
    """
    Render the email notification template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for email notification.
    """
    return render(request, 'vest_store_app/email_notification.html')

def send_email(request):
    """
    Send a test email notification.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for email notification.
    """
    subject = 'Test Email Notification'
    message = 'This is a test email notification.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['iylamsriramteja@gmail.com']

    send_mail(subject, message, email_from, recipient_list)
    
    return render(request, 'vest_store_app/email_notification.html') 



def home(request):
    # Retrieve all vest objects from the database
    """
    Render the home page template and send low stock email notifications.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for the home page.
    """
    count = 0
    vests = Vest.objects.all()
    email_sent = False  # Flag to track if the email has been sent
    dict = {}

    for vest in vests:
        count += 1
        if vest.stock < 5:
            
            # Update the dictionary with the size and stock of the vest
            dict[vest.size] = vest.stock
            
            # Check if 3 vests with low stock have been found
            if count == 3 and not email_sent:
                print(dict)
                # Compose your email message
                subject = 'Low Stock Notification'
                message = 'Please stock your vests, The following vests are running out of stock:\n'
                for size, stock in dict.items():
                    message += f'Size: {size}, Stock: {stock}\n'
                recipient_list = ['iylamsriramteja@gmail.com']
                email_from = settings.EMAIL_HOST_USER
                message2 = 'Reply to this email, for any further assistance'
                msg = message+message2
                # Send the email
                send_mail(subject, msg, email_from,  recipient_list)
                email_sent = True  # Set the flag to True to avoid sending multiple emails
                break  # Exit the loop after sending the email

            else: continue

    # Render your home template
    return render(request, 'vest_store_app/home.html', {'vests': vests})

def about_page(request):
    """
    Render the about page template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for the about page.
    """
    return render(request, 'vest_store_app/about.html')

def cart_page(request):
    """
    Render the cart page template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for the cart page with the current cart data.
    """
    cart = request.session.get('cart', {})
    
    return render(request, 'vest_store_app/cart.html', {'cart': cart})



def add_to_cart(request, quantity, size):
    """
    Add a vest item to the cart.

    Parameters:
    - request: The HTTP request object.
    - quantity: The quantity of the vest item to add.
    - size: The size of the vest item to add.

    Returns:
    - Redirects to the cart page after adding the item to the cart.
    """
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
    """
    Delete a vest item from the cart.

    Parameters:
    - request: The HTTP request object.
    - size: The size of the vest item to delete from the cart.

    Returns:
    - Redirects to the cart page after deleting the item from the cart.
    """
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
     
    """
    Placeholder for checkout logic.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for the checkout page.
    """
    # Your checkout logic goes here
    return render(request, 'vest_store_app/checkout.html')


def order_confirmation(request):
    """
    Process the order confirmation.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered template for the order confirmation page with purchased items and total price.
    """
    # Retrieve purchased items from the session
    cart = request.session.get('cart', {})
    purchased_items = []

    # Retrieve details of purchased vests based on items in the cart
    total_price = 0
    for size, quantity in cart.items():
        vest = Vest.objects.get(size=size)
        total_price += vest.price * quantity
        purchased_items.append({'vest': vest, 'quantity': quantity})

        vest = Vest.objects.get(size=size)
        vest.stock -= quantity
        vest.save()


    # Clear the cart after displaying items in order confirmation
    request.session['cart'] = {}

    return render(request, 'vest_store_app/order_confirmation.html', {'purchased_items': purchased_items, 'total_price': total_price})

def store_user_details(request):
    """
    Store user details in the database.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - JSON response indicating success or failure.
    """
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

def get_cart_item_count(request):
    """
    Get the total count of items in the cart.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - JSON response containing the total count of items in the cart.
    """
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return JsonResponse({'count': total_items})