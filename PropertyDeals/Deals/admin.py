from django.contrib import admin
from .models import PropertyType, Property, PropertyImages, PropertyInvestmentType, UkTownAndCounty, UkPostcode
# Register your models here.
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(PropertyInvestmentType)

admin.site.register(UkTownAndCounty)
admin.site.register(UkPostcode)
