from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
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

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def account_details(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'bank/account.html', {'account': account})