from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,'Deals/landing_page.html')
