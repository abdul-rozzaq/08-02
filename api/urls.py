from django.urls import path

from .views import (ClassAPIView, ClassDetailAPIView, HotelAPIView,
                    HotelDetailAPIView, TravelAPIView, TravelDetailAPIView)

urlpatterns = [
    path('travels/', TravelAPIView.as_view(), name='travels-list'),
    path('travels/<int:pk>/', TravelDetailAPIView.as_view(), name='travels-detail'),
    
    path('classes/', ClassAPIView.as_view(), name='classes-list'),
    path('classes/<int:pk>/', ClassDetailAPIView.as_view(), name='classes-detail'),
    
    path('hotels/', HotelAPIView.as_view(), name='hotels-list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotels-detail'),
]


