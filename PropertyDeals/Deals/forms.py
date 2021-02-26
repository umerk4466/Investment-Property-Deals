from django import forms
from Deals.choise_field_lists import PRICE_LIST,BEDROOM_LIST

class SearchDeal(forms.Form):
    place = forms.CharField(label="Search using 'town name', 'postcode'",max_length=255, 
                    widget=forms.TextInput(attrs={'placeholder': 'e.g. ‘York’, ‘LU3’ or ‘LU21HT’'}))
    min_price_choises = forms.ChoiceField(label="Min Price (£)", choices = PRICE_LIST, initial='0', required = False)
    max_price_choises = forms.ChoiceField(label="Max Price (£)", choices = PRICE_LIST, initial='0', required = False,)
    min_bedroom = forms.ChoiceField(label="Min Bedroom", choices = BEDROOM_LIST, initial='0', required = False,)
    max_bedroom = forms.ChoiceField(label="Max Bedroom", choices = BEDROOM_LIST, initial='0', required = False,)


