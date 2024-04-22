from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about_page, name="about_page"),
    path('cart/', views.cart_page, name='cart_page'),
    path('add_to_cart/<int:quantity>/<str:size>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<str:size>/', views.delete_from_cart, name='delete_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
]