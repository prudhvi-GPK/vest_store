# test_models.py

from django.test import TestCase
from ..models import Vest, UserDetails

class VestModelTestCase(TestCase):
    def setUp(self):
        Vest.objects.create(size='S', price=12.99, stock=5)
        Vest.objects.create(size='M', price=12.99, stock=0)
        Vest.objects.create(size='L', price=14.99, stock=15)

    def test_vest_creation(self):
        small_vest = Vest.objects.get(size='S')
        medium_vest = Vest.objects.get(size='M')
        large_vest = Vest.objects.get(size='L')

        self.assertEqual(small_vest.get_size_display(), 'Small')
        self.assertEqual(medium_vest.get_size_display(), 'Medium')
        self.assertEqual(large_vest.get_size_display(), 'Large')

        self.assertEqual(small_vest.price, '12.99')
        self.assertEqual(medium_vest.price, '12.99')
        self.assertEqual(large_vest.price, '14.99')

        self.assertEqual(small_vest.stock, 5)
        self.assertEqual(medium_vest.stock, 0)
        self.assertEqual(large_vest.stock, 15)

class UserDetailsModelTestCase(TestCase):
    def setUp(self):
        UserDetails.objects.create(name='John Doe', phone='1234567890', email='john@example.com')

    def test_user_details_creation(self):
        user_details = UserDetails.objects.get(name='John Doe')

        self.assertEqual(user_details.name, 'John Doe')
        self.assertEqual(user_details.phone, '1234567890')
        self.assertEqual(user_details.email, 'john@example.com')
