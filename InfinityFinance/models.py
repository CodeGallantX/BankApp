from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender_transactions')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
