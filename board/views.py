from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from board.models import Job, Candidate
from board.forms import JobForm, CandidateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .filters import JobFilter
from django_filters.views import FilterView


# ALL LIST FUNCTIONS  (1)
def Job_list(request):
    # Retrieve all records from the database
    jobs = Job.objects.all()
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs
    paginator = Paginator(jobs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # Render a template with the records
    context = {'jobs': page_obj, 'count': Job.objects.all().count,
               'myfilter': myfilter}
    return render(request, 'board/job_list.html', context)
# CBV


class JobList(ListView):
    paginate_by = 4
    model = Job
    context_object_name = 'jobs'
    extra_context = {'count': Job.objects.all().count}


# ___________________________________________________
# FUNCTIONS    (2)


def Job_detail(request, slug):
    # Retrieve a specific record by ID
    job = get_object_or_404(Job, slug=slug)
    # Render a template with the record
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            Candidate = form.save(commit=False)
            Candidate.job = job
            Candidate.save()
            return redirect('board:job_detail', slug=job.slug)
    # Render a form for creating a new record
    else:
        form = CandidateForm()
    context = {'job': job, 'form': form}
    return render(request, 'board/job_detail.html', context)
# CBV


class JobDetail(DetailView):
    model = Job

# ___________________________________________________

# FUNCTIONS    (3)


def Job_create(request):
    # Handle form submission for creating a new record
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('board:job_detail', slug=job.slug)
    # Render a form for creating a new record
    else:
        form = JobForm()
        return render(request, 'board/job_create.html', {'form': form})
# CBV


class JobCreate(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'board/job_create.html'
    success_url = reverse_lazy('board:job_list')
# ___________________________________________________

# FUNCTIONS (4)


def Job_update(request, slug):
    # Retrieve a specific record by ID
    job = get_object_or_404(Job, slug=slug)

    # Handle form submission for updating the record
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('board:job_detail', slug=job.slug)
    # Render a form for updating the record
    else:
        form = JobForm(instance=job)
        return render(request, 'board/job_update.html', {'form': form})

# CBV


class JobUpdate(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'board/job_update.html'
    success_url = reverse_lazy('board:job_list')

# _____________________________________________________

# FUNCTIONS  (5)


def Job_delete(request, slug):
    # Retrieve a specific record by ID
    job = get_object_or_404(Job, slug=slug)

    # Handle form submission for deleting the record
    if request.method == 'POST':
        job.delete()
        return redirect('board:job_list')
    # Render a confirmation form for deleting the record
    else:
        return render(request, 'board/job_delete.html', {'job': job})

# CBV


class JobDelete(DeleteView):
    model = Job
    template_name = 'board/job_delete.html'
    success_url = reverse_lazy('board:job_list')
