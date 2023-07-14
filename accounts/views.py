from django.shortcuts import render
from .forms import ProfileForm,UserForm,SignUpForm
from.models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # email=request.POST['email']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # return redirect(reverse('board:jobs'))
#         else:
#             # authentication failed
#             return render(request, 'registration/login.html', {'error': True})
#     else:
#         return render(request, 'registration/login.html')


def signUp(request):
    if request.method=='POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request,username=username, password=password)
            login(request,user)
            return redirect ('accounts:profile')
    else:
        form=SignUpForm()
    
    return render(request,'accounts/signup.html',{'form':form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             email=form.cleaned_data['email']
#             user = authenticate(username=username, password=password,email=email)
#             login(request,user)
#             return redirect ('accounts:profile')
#     else:
#         form = UserCreationForm()
#     return render(request,'accounts/signup.html', {'form': form})
# # 


def MyProfile(request):
    profile=Profile.objects.get(user=request.user)
    # print('done  ...........')
    return render(request,'accounts/profile.html',{'profile':profile})

def MyProfileEdit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        user_Form=UserForm(request.POST,request.FILES,instance=profile.user)
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)
        if profile_form.is_valid()  and  user_Form.is_valid() :
            user_Form.save()
            my_profile=profile_form.save(commit=False)
            my_profile.user=request.user
            profile_form.save()
            return redirect(reverse('accounts:profile'))
        
    else:
        user_Form=UserForm(instance=profile.user)
        profile_form=ProfileForm(instance=profile)
    return render (request,'accounts/profile_edit.html',{'user_Form':user_Form,'profile_form':profile_form})
        
        
from django.contrib.auth.views import PasswordResetView

# class CustomPasswordResetView(PasswordResetView):
#     subject_template_name = 'password_reset_subject.txt'
#     email_template_name = 'password_reset_email.html'
#     success_url = 'accounts/ password_reset/done'