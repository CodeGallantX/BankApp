from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('InfinityFinance.urls')),
    path('admin/', admin.site.urls),
    path('', infinity_views.home_page, name=''),  # Use infinity_views to access the views
    path('account/', infinity_views.account, name='account'),
    path('transfer/', infinity_views.transfer, name='transfer'),
    path('deposit/', infinity_views.deposit, name='deposit'),
    path('withdraw/', infinity_views.withdraw, name='withdraw'),
    path('register/', infinity_views.RegisterView.as_view(), name="signup"),
    path('account/<int:account_id>/', infinity_views.account_details, name="account_details"),
]

handler404 = 'InfinityFinance.views.page_not_found'  # Correct the handler404 to use the correct module path
