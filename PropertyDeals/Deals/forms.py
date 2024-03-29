from django import forms
from Deals.choise_field_lists import PRICE_LIST,BEDROOM_LIST
from .models import PropertyType, PropertyInvestmentType

class SearchDeal(forms.Form):
    location = forms.CharField(label="Search using 'town name', 'postcode'",max_length=255, widget=forms.TextInput(attrs={'placeholder': "e.g. ‘York’, ‘LU3’ or ‘LU21HT",
            'data-url': "http://127.0.0.1:8000/location_autocomplete/", 'data-noresults-text':'No matches found', 'autocomplete':'off'}))
    min_price = forms.ChoiceField(label="Min Price (£)", choices = PRICE_LIST, initial='0', required = False)
    max_price = forms.ChoiceField(label="Max Price (£)", choices = PRICE_LIST, initial='0', required = False,)
    min_bedroom = forms.ChoiceField(label="Min Bedroom", choices = BEDROOM_LIST, initial='0', required = False,)
    max_bedroom = forms.ChoiceField(label="Max Bedroom", choices = BEDROOM_LIST, initial='0', required = False,)
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), to_field_name="name", empty_label="All Types", required = False,) 
    Property_investment_type = forms.ModelChoiceField(queryset=PropertyInvestmentType.objects.all(), to_field_name="name", empty_label="All Types", required = False,) 
