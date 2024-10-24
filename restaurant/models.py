from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)  # Name of the menu item
    description = models.TextField()  # Description of the menu item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item
    available = models.BooleanField(default=True)  # Availability of the item

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField()  # Customer's email
    date = models.DateTimeField()  # Date and time of the booking
    number_of_guests = models.IntegerField()  # Number of guests
    special_requests = models.TextField(blank=True)  # Special requests, if any

    def __str__(self):
        return f'Booking for {self.name} on {self.date}'
