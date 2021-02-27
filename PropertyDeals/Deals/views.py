from django.shortcuts import render, redirect
from .forms import SearchDeal


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