# models.py
from django.db import models

class Vest(models.Model):
    """
    Represents a vest item in the store.

    Attributes:
    - size (str): The size of the vest (S, M, L).
    - price (Decimal): The price of the vest.
    - stock (PositiveIntegerField): The available stock of the vest.
    """
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    """
        Returns a string representation of the vest item.

        Returns:
            str: A string representing the vest item with size, price, and stock.
    """
    def __str__(self):
        return f"{self.get_size_display()} - Price: ${self.price} - Stock: {self.stock}"
class UserDetails(models.Model):
    """
    Represents user details for the store.

    Attributes:
    - name (str): The name of the user.
    - phone (str): The phone number of the user.
    - email (EmailField): The email address of the user.
    """
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    """
        Returns a string representation of the user details.

        Returns:
            str: A string representing the user's name.
    """
    def __str__(self):
        return self.name