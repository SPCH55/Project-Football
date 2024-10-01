from django.db import models
from django.contrib.auth.models import User
class FootballField(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

class FieldBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.field_name} on {self.booking_date} at {self.booking_time}"
    
# *********NEW*******
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.field_name} on {self.booking_date} at {self.booking_time}"