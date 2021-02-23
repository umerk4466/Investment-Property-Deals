from django.shortcuts import render, redirect
from .forms import InvestorSignup, DealSourcerSignup
from .models import User, DealSourcer, Profile



# Create your views here.
def landing_page(request):
    return render(request,'Accounts/landing_page.html')

def investor_signup(request):
    if request.method == 'POST':
        form = InvestorSignup(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            user.user_type = 1 # 1:Investor, 2:Deal sorcer, 3:Admin, 4:Super admin
            user.save()
            return redirect('login')
    else:
        form = InvestorSignup()
    return render(request, 'Accounts/investor_signup.html', {'form': form})




def deal_sourcer_signup(request):
    if request.method == 'POST':
        form = DealSourcerSignup(request.POST)
        post_code = request.POST.get('post_code')
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            user.user_type = 2 # 1:Investor, 2:Deal sorcer, 3:Admin, 4:Super admin
            user.save()
            # add post_code to user profile
            user_profile = Profile.objects.get(user=user)
            user_profile.post_code = post_code
            user_profile.save()
            # create DealSourcer model's object
            deal_sourcer = DealSourcer.objects.create(user=user)
            deal_sourcer.save()
            return redirect('login')
    else:
        form = DealSourcerSignup()
    return render(request, 'Accounts/deal_sourcer_signup.html', {'form': form})