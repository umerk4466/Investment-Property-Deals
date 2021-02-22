from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='Accounts/home.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Accounts/logout.html'), name='logout'),
    path('accounts/investor/', views.investor_signup, name='investor_signup'),
    path('accounts/deal-sourcer/', views.deal_sourcer_signup, name='deal_sourcer_signup'),


]