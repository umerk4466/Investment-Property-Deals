from django.contrib import admin
from .models import PropertyType, Property, PropertyInvestmentType, UkTownAndCounty, UkPostcode
# Register your models here.
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(PropertyInvestmentType)

admin.site.register(UkTownAndCounty)
admin.site.register(UkPostcode)
