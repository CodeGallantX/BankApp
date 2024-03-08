from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, RegisterView
from django.urls import reverse_lazy
from .models import Account

# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def missing_404_page(request, exception):
    return render(request, '404.html', status=404)


class CustomLoginView(LoginView):
    template_name = 'bank/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class CustomRegisterView(RegisterView):
    template_name = 'bank/register.html'
    success_url = reverse_lazy('login')