from django.urls import path
from .views import CustomLoginView  # นำเข้า CustomLoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import confirm_booking

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logouts', views.logout_view, name='logout'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bookings', views.bookings, name='bookings'),
    path('contact', views.contact, name='contact'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('confirm_booking/', views.confirm_booking, name='confirm_booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

