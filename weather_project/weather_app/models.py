from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.DecimalField(max_digits=6, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation_index = models.DecimalField(max_digits=5, decimal_places=2)
    weather_condition = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} - {self.weather_condition}"
