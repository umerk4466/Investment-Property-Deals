from django.contrib import admin
from .models import PropertyType, Property, UkTownAndCounty, UkPostcode
# Register your models here.
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(UkTownAndCounty)
admin.site.register(UkPostcode)
