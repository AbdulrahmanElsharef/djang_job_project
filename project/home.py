
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from companies.models import Employer as EM
from companies.forms import EmployerForm
from companies.filters import EmployerFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from board.models import Job

def main(request):
    return render(request,'main.html',{})

