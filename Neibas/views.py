from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.views import generic


# Create your views here.

def home(request):
    neibas = Neiba.objects.all()
    
    return render(request,"home.html",locals())

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, f'Your account has been updated')
            return render(request,'profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'profile.html',locals())



def hood(request):
    current_user = request.user
    if request.method == "POST":
        form = NeibaForm(request.POST, request.FILES)
        if form.is_valid():
            neiba = form.save(commit=False)
            neiba.user = current_user
            neiba.save()
        return redirect("home")

    else:
        form = NeibaForm()
    return render(request, "hood.html",locals())
