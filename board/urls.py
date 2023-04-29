from django.contrib import admin
from django.urls import path, include
from .views import *


app_name='board'

urlpatterns = [
    path('jobs/', JobList.as_view() ,name='job_list'),
]