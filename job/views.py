from django.shortcuts import render

# Create your views here.
from .models import Job


def all_jobs(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)


def job_details(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {'job': job}
    return render(request, 'job_details.html', context)
