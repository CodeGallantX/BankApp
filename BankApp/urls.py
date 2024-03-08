from django.contrib import admin
from django.urls import path, include
from InfinityFinance.views import home_page
from InfinityFinance import views as finance_views

app_name = 'bank'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('account/', finance_views.account, name='account'),
    path('transfer/', finance_views.transfer, name='transfer'),
    path('deposit/', finance_views.deposit, name='deposit'),
    path('withdraw/', finance_views.withdraw, name='withdraw'),
    path('register/', finance_views.signup, name="signup"),
    path('account/<int:account_id>/', finance_views.account_details, name="account_details"),
]


handler404 = 'InfinityFinance.views.page_not_found'