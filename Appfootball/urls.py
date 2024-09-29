from django.urls import path
from .views import CustomLoginView  # นำเข้า CustomLoginView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logouts', views.logout_view, name='logout'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('bookings', views.bookings, name='bookings'),
    path('contact', views.contact, name='contact'),
]

