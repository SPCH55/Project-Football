from django.db import models

class FootballField(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
