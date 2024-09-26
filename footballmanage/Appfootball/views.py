from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm  # นำเข้าฟอร์มที่สร้างขึ้น
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'  

def home_view(request):
    return render(request, 'home.html')


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


