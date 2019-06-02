from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate




# Create your views here.



# @login_required(login_url="/accounts/login/")
def home(request):
    # hoods = Hood.objects.all()
    
    return render(request,"home.html",locals())

