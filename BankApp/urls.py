"""
URL configuration for BankApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for BankApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

app_name = 'bank'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 'InfinityFinance.views.home_page', name='home'),
    path('account/', 'InfinityFinance.views.account', name='account'),
    path('transfer/', 'InfinityFinance.views.transfer', name='transfer'),
    path('deposit/', 'InfinityFinance.views.deposit', name='deposit'),
    path('withdraw/', 'InfinityFinance.views.withdraw', name='withdraw'),
    path('register/', 'InfinityFinance.views.signup', name="signup"),
    path('account/<int:account_id>', account_details, name="account_details")
    
]
    # Add more URL patterns for other views as needed
handler404 = 'InfinityFinance.views.page_not_found'