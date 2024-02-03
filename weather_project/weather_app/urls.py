# weather_api/urls.py

from django.urls import path
from .views import WeatherDataListCreateView

urlpatterns = [
    path('weather/', WeatherDataListCreateView.as_view(), name='weather-list-create'),
]
