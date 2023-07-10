from django.shortcuts import render
from .forms import SignUpForm,ProfileForm,UserForm
from.models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
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
    profile=Profile.objects.get(user=request.user)
    print('done  ...........')
    return render(request,'accounts/profile.html',{'profile':profile})

def MyProfileEdit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        user_Form=UserForm(request.POST,request.FILES,instance=request.user)
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid()  and user_Form.is_valid() :
            user_Form.save()
            myprofile=profile_form.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
        
    else:
        user_Form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=profile)
    return render (request,'accounts/profile_edit.html',{'user_Form':user_Form,'profile_form':profile_form})
        