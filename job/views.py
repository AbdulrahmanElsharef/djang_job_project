from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
from .forms import ApplyForm,JobForm

# Create your views here.
from .models import Job, Apply_job


def all_jobs(request):
    jobs = Job.objects.all()
    # paginator = Paginator(jobs, 10)  # Show 25 contacts per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)


def job_details(request, job_slug):
    detail = Job.objects.get(slug=job_slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = detail
            myform.save()
            # print('done')
    else:
        form = ApplyForm()
    context = {'job':detail ,"apply": form}
    return render(request, 'job_details.html', context)


def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
    else:
        form = JobForm()
    context = {"add": form}
    return render(request, 'post_job.html', context)


def del_job(request, job_slug):
    job = Job.objects.get(slug=job_slug)
    job.delete()
    return redirect('/jobs')
