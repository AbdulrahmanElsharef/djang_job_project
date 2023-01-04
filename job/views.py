from django.shortcuts import render

# Create your views here.
from .models import Job, category


def all_jobs(request):
    jobs=Job.objects.all()
    return render(request,'index.html',{'objects':jobs})
    pass


def job_details(request, job_id):
    details=Job.objects.get(id=job_id)
    return render(request,'job_details.html',{'obj':details})

