from django.urls import path
from django.contrib import admin
from . import views 

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about_page, name="about_page"),
    path('cart/', views.cart_page, name='cart_page'),
    path('add_to_cart/<int:quantity>/<str:size>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('delete_from_cart/<str:size>/', views.delete_from_cart, name='delete_from_cart'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('email_notification/', views.email_notification, name='email_notification'),
    path('send_email/', views.send_email, name='send_email'),
    path('get_cart_item_count/', views.get_cart_item_count, name='get_cart_item_count'),
]

