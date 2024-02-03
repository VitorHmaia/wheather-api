# weather_api/views.py

from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
