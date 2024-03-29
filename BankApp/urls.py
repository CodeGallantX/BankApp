from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from InfinityFinance import views as infinity_views  # Import the views from InfinityFinance app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/custom_admin_login.html'), name='admin_login'),
    path('', infinity_views.home, name=''),  # Use infinity_views to access the views
    path('account/', infinity_views.account, name='account'),
    path('transfer/', infinity_views.transfer, name='transfer'),
    path('deposit/', infinity_views.deposit, name='deposit'),
    path('withdraw/', infinity_views.withdraw, name='withdraw'),
    path('register/', infinity_views.RegisterView.as_view(), name="signup"),
    path('account/<int:account_id>/', infinity_views.account_details, name="account_details"),
]

handler404 = 'InfinityFinance.views.error_404'  # Correct the handler404 to use the correct module path
