from django.urls import path
from django.contrib import admin
from . import views 

urlpatterns = [
     path('admin/', admin.site.urls),#/admin/: Admin site URLs.
    path('', views.home, name='home'),# /: Home page URL.
    path('about/', views.about_page, name="about_page"),#  /about/: About page URL.
    path('cart/', views.cart_page, name='cart_page'),# /cart/: Shopping cart page URL.
    path('add_to_cart/<int:quantity>/<str:size>/', views.add_to_cart, name='add_to_cart'),# /add_to_cart/<int:quantity>/<str:size>/: Add to cart URL with quantity and size parameters.
    path('checkout/', views.checkout, name='checkout'), #/checkout/: Checkout page URL.
    path('delete_from_cart/<str:size>/', views.delete_from_cart, name='delete_from_cart'),#/delete_from_cart/<str:size>/: Delete from cart URL with size parameter.
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),#/order_confirmation/: Order confirmation page URL.
    path('email_notification/', views.email_notification, name='email_notification'),# /email_notification/: Email notification page URL.
    path('send_email/', views.send_email, name='send_email'),#/send_email/: Send email notification URL.
    path('get_cart_item_count/', views.get_cart_item_count, name='get_cart_item_count'), #/get_cart_item_count/: Get cart item count URL.
]

