from django.urls import path
from .views import CustomLoginView  # นำเข้า CustomLoginView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logouts/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('bookings/', views.bookings_view, name='bookings'),
]

