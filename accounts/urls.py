from django.urls import path
from .views import signUp

app_name='accounts'

urlpatterns = [
    path('signup', signUp ,name='signup'),  #functions
    path('profile', signUp ,name='profile'),  #functions
]