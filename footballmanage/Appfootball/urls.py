from django.urls import path
from .views import CustomLoginView  # นำเข้า CustomLoginView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logouts/', views.logout_view, name='logout'),
]
