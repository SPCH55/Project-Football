from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm  # นำเข้าฟอร์มที่สร้างขึ้น
from django.shortcuts import render


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'  

def home_view(request):
    return render(request, 'home.html')
