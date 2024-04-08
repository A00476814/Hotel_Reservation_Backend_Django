from django.urls import path
from .views import HotelList

urlpatterns = [
    path('hotels/', HotelList.as_view(), name='hotel-list'),
]