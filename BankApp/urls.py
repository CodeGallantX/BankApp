from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from InfinityFinance.views import home_page, account_details

app_name = 'bank'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InfinityFinance.views.home_page, name='home'),
    path('account/', InfinityFinance.views.account, name='account'),
    path('transfer/', InfinityFinance.views.transfer, name='transfer'),
    path('deposit/', InfinityFinance.views.deposit, name='deposit'),
    path('withdraw/', InfinityFinance.views.withdraw, name='withdraw'),
    path('register/', InfinityFinance.views.signup, name="signup"),
    path('account/<int:account_id>/', InfinityFinance.views.account_details, name="account_details"),
]

handler404 = 'InfinityFinance.views.page_not_found'