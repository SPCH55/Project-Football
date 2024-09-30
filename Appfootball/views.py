from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import FieldBooking
from .forms import FieldBookingForm
from django.http import HttpResponse

# def bookings_view(request):
#     return render(request, 'bookings.html')

# def about_view(request):
#     return render(request, 'about.html')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'  

# def home_view(request):
#     return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # กลับไปหน้าแรกหลังจากล็อกอิน
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # เปลี่ยนเป็น URL ที่คุณต้องการให้ผู้ใช้ไปหลังลงทะเบียน
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bookings(request):
    return render(request, 'bookings.html')

def contact(request):
    return render(request, 'contact.html')

def userprofile(request):
    return render(request, 'userprofile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def change_password(request):
    return render(request, 'change_password.html')  # ตรวจสอบชื่อไฟล์ให้ตรง

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
        
def edit_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        profile_image = request.FILES.get('profile_image')

        # สมมุติว่าคุณมีโมเดล UserProfile สำหรับเก็บข้อมูลโปรไฟล์
        user_profile = request.user.profile
        user_profile.username = username
        user_profile.email = email

        if profile_image:
            user_profile.profile_image = profile_image

        user_profile.save()
        return redirect('profile')  # เปลี่ยนเป็น URL ของหน้าโปรไฟล์

    return render(request, 'edit_profile.html')



@login_required
def confirm_booking(request):
    if request.method == 'POST':
        field_name = request.POST.get('field_name')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')

        # สร้างอ็อบเจกต์การจองและบันทึกลงฐานข้อมูล
        booking = FieldBooking(user=request.user, field_name=field_name, 
                               booking_date=booking_date, booking_time=booking_time)
        booking.save()

        return HttpResponse('การจองของคุณได้รับการยืนยันแล้ว')

    return redirect('home')


