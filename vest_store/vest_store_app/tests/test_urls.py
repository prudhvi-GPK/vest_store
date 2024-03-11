import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'vest_store.settings'
from django.test import TestCase
from django.urls import reverse
import sys
print(sys.path)
from vest_store_app.views import home, about_page, cart_page,add_to_cart

class UrlTests(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vest_store_app/home.html')

    def test_about_page_url(self):
        response = self.client.get(reverse('about_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vest_store_app/about.html')

    def test_cart_page_url(self):
        response = self.client.get(reverse('cart_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vest_store_app/cart.html')

    def test_add_to_cart_url(self):
        quantity = 2
        size = 'medium'
        response = self.client.get(reverse('add_to_cart', args=(quantity, size)))
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect
        self.assertRedirects(response, reverse('cart_page'))

    def test_add_to_cart_url_with_valid_arguments(self):
        response = self.client.get(reverse('add_to_cart', args=(1, 'medium')))
        self.assertEqual(response.status_code, 302)  # Assuming you handle valid sizes with a redirect
        self.assertRedirects(response, reverse('cart_page'))

    def test_add_to_cart_url_with_invalid_size(self):
        response = self.client.get(reverse('add_to_cart', args=(1, 'invalid_size')))
        self.assertEqual(response.status_code, 302) 
