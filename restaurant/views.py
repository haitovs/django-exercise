from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


class MenuListCreate(generics.ListCreateAPIView):
    """
    View to list and create Menu instances.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a Menu instance.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingListCreate(generics.ListCreateAPIView):
    """
    View to list and create Booking instances.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a Booking instance.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
