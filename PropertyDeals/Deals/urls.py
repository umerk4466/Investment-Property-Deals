from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('search/', views.search_property, name='search_property'),
    path("location_autocomplete/", views.location_autocomplete, name='location_autocomplete'),
]