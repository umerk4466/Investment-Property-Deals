from django.shortcuts import render, redirect
from .forms import SearchDeal
from .models import UkTownAndCounty, UkPostcode

from django.http import HttpResponse, JsonResponse
from itertools import chain

# Create your views here.
def landing_page(request):
    if request.method == 'POST':
        serch_form = SearchDeal(request.POST)
        if serch_form.is_valid():
            return redirect('login')
    else:
        serch_form = SearchDeal()
    return render(request,'Deals/landing_page.html', {'serch_form': serch_form})

def search_property(requests):
    pass


def location_autocomplete(request):
    if request.GET.get('q') and request.is_ajax():
        q = request.GET['q']
        town_county = UkTownAndCounty.objects.filter(town_and_county__istartswith=q).values_list('town_and_county', flat=True)[:5]
        postcode = UkPostcode.objects.filter(postcode__istartswith=q).values_list('postcode', flat=True)[:5]
        json = list(chain(town_county, postcode))
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("None")



# csv to django model imports
import csv
import os
from django.conf import settings

def create_csv_uk_town_county():
     with open(os.path.join(settings.BASE_DIR,'Deals', 'places', 'uk_towns_and_counties.csv')) as f:
        reader = csv.reader(f)
        for row in reader:
            created = UkTownAndCounty.objects.get_or_create(
                town_and_county=row[1]+", "+row[2],
                )

def create_csv_uk_postcode():
     with open(os.path.join(settings.BASE_DIR,'Deals', 'places', 'uk_postcode_and_latitude_longitude.csv')) as f:
        reader = csv.reader(f)
        for row in reader:
            created = UkPostcode.objects.get_or_create(
                postcode=row[1],
                )

