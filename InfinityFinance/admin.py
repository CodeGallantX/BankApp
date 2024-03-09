from django.contrib import admin
from .models import Account, Transaction

# Register your models here.


# Creating Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = 'Custom Admin Site'
    site_title = 'Custom Admin Site'

IF_admin_site = CustomAdminSite(name='IF_admin')

# Register your models with the custom admin site
IF_admin_site.register(Account)
IF_admin_site.register(Transaction)

