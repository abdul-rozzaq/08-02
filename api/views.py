from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Class, Hotel, Travel
from .serializers import ClassSerializer, HotelSerializer, TravelSerializer


class TravelAPIView(ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer


class TravelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer


class ClassAPIView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class HotelAPIView(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
