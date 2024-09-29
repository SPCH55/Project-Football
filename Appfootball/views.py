from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import RegistrationForm

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

