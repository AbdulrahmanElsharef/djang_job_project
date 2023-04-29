from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.generic import ListView



class JobList(ListView):
    model=Job
    # template_name='base.html'


