from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from ..views import home, about_page, cart_page, add_to_cart

class ViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vest_store_app/home.html')

    def test_about_page_view(self):
        response = self.client.get(reverse('about_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vest_store_app/about.html')

    def test_cart_page_view_empty_cart(self):
        response = self.client.get(reverse('cart_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vest_store_app/cart.html')
        self.assertContains(response, 'Your cart is empty')



    def test_add_to_cart_view(self):
        
        # Using Django's Client to handle sessions
        client = Client()

        # Simulate a request with specific parameters
        response = client.get(reverse('add_to_cart', args=(1, 'medium')))
        self.assertEqual(response.status_code, 302)  # Assuming you handle valid sizes with a redirect
        self.assertRedirects(response, reverse('cart_page'))

        # Test the cart content after adding an item
        cart = client.session.get('cart', {})
        self.assertIn('vest_medium', cart)
        self.assertEqual(cart['vest_medium'], 1)


    

