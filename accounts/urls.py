from django.urls import path
from .views import signUp,MyProfile,MyProfileEdit

app_name='accounts'

urlpatterns = [
    path('signup', signUp ,name='signup'),  #functions
    path('profile', MyProfile ,name='profile'),  #functions
    path('profile/edit', MyProfileEdit ,name='profile_edit'),  #functions
]