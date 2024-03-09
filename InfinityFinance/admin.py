from django.contrib import admin
from .models import Account, Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)

# Creating Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = 'Custom Admin Site'
    site_title = 'Custom Admin Site'

custom_admin_site = CustomAdminSite(name='custom_admin')
