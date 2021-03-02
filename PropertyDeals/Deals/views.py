from django.shortcuts import render, redirect
from .forms import SearchDeal
from .models import PlacesUk

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
        city = PlacesUk.objects.filter(city__icontains=q).values_list('city', flat=True)
        postcode = PlacesUk.objects.filter(postcode__icontains=q).values_list('postcode', flat=True)
        json = list(chain(city, postcode))
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("None")