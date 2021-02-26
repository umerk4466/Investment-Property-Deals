from django import forms
from Deals.price_lists import PRICE_LIST

class SearchDeal(forms.Form):
    place = forms.CharField(label="Search using 'town name', 'postcode'",max_length=255, 
                    widget=forms.TextInput(attrs={'placeholder': 'e.g. ‘York’, ‘LU3’ or ‘LU21HT’'}))
    min_price_choises = forms.ChoiceField(choices = PRICE_LIST, initial='01', required = True,)