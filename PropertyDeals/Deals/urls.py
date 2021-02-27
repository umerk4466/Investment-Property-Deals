from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('search/location=luton&min_price=1&max_price=2&property_type=Buy+To+Let&max_bedroom=1', views.search_property, name='search_property'),

]