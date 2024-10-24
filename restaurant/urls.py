from django.urls import path
from .views import MenuListCreate, MenuDetail, BookingListCreate, BookingDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('menu/', MenuListCreate.as_view(), name='menu-list-create'),  # URL for listing and creating Menu items
    path('menu/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),  # URL for retrieving, updating, or deleting a Menu item
    path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),  # URL for listing and creating Booking items
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),  # URL for retrieving, updating, or deleting a Booking item
]
