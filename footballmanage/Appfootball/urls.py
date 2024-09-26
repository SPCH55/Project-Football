from django.urls import path
from .views import CustomLoginView  # นำเข้า CustomLoginView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),  # ใช้ CustomLoginView ที่สร้างขึ้น
]
