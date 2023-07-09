from django.shortcuts import render
from .forms import SignUpForm
from.models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
# Create your views here.
def signUp(request):
    if request.method=='POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect ('accounts:profile')
    else:
        form=SignUpForm()
    
    return render(request,'accounts/signup.html',{'form':form})


def MyProfile(request):
    profile=Profile.objects.last()
    return render(request,'accounts/profile.html',{'profile':profile})