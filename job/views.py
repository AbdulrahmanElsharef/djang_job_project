from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm

# Create your views here.
from .models import Job, Apply_job


def all_jobs(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)


def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('/jobs')
    else:
        form = JobForm()
    context = {"add": form}
    return render(request, 'post_job.html', context)


def job_details(request, job_slug):
    detail = Job.objects.get(slug=job_slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = detail
            myform.save()
            return redirect('/jobs')
    else:
        form = ApplyForm()
    context = {'job': detail, "apply": form}
    return render(request, 'job_details.html', context)


# def del_job(request, job_slug):
#     job = Job.objects.get(slug=job_slug)
#     job.delete()
#     return redirect('/jobs')

def candidates(request):
    persons = Apply_job.objects.all()
    context = {'candidates': persons}
    print('done dddddddddddd')
    return render(request, 'candidates.html', context)
