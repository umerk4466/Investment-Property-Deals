from django.shortcuts import render, redirect
from .forms import InvestorSignup
from .models import Investor, User



# Create your views here.
def home(request):
    return render(request,'Accounts/home.html')




def investor_signup(request):
    if request.method == 'POST':
        form = InvestorSignup(request.POST)
        post_code = request.POST.get('post_code')
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            user.user_type = 1 # 1:Investor, 2:Deal sorcer, 3:Admin, 4:Super admin
            user.save()
            investor = Investor.objects.create(user=user, post_code=post_code)
            investor.save()
            return redirect('login')
    else:
        form = InvestorSignup()
    return render(request, 'Accounts/investor_signup.html', {'form': form})