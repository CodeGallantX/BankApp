from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Account

def home_page(request):
    return render(request, 'bank/homepage.html')

def page_not_found(request):
    return render(request, '404.html', status=404)

def account(request):
    # Your logic for account view
    return render(request, 'bank/account.html')

def transfer(request):
    # Your logic for transfer view
    return render(request, 'bank/transfer.html')

def deposit(request):
    # Your logic for deposit view
    return render(request, 'bank/deposit.html')

def withdraw(request):
    # Your logic for withdraw view
    return render(request, 'bank/withdraw.html')

class CustomLoginView(LoginView):
    template_name = 'bank/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def account_details(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'bank/account_details.html', {'account': account})
