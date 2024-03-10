from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name="about_page"),
    path('cart/', views.cart_page, name='cart_page'),
    path('add_to_cart/<int:quantity>/<str:size>/', views.add_to_cart, name='add_to_cart'),
]