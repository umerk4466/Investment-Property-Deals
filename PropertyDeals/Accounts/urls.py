from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login', auth_views.LoginView.as_view(template_name='Accounts/login.html', authentication_form=UserLoginForm ,redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'), name='logout'),
    path('accounts/investor/', views.investor_signup, name='investor_signup'),
    path('accounts/deal-sourcer/', views.deal_sourcer_signup, name='deal_sourcer_signup'),
]