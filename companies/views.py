from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from companies.models import Employer as EM
from companies.forms import EmployerForm
from companies.filters import EmployerFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from board.models import Job
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


# ALL LIST FUNCTIONS  (1)
def Employer_list(request):
    # Retrieve all records from the database
    Employers = EM.objects.all()
    myfilter = EmployerFilter(request.GET, queryset=Employers)
    Employers = myfilter.qs
    paginator = Paginator(Employers, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # Render a template with the records
    context = {'Employers': page_obj, 'count': EM.objects.all().count,
               'myfilter': myfilter}
    return render(request, 'companies/employer_list.html', context)
# CBV


class EmployerList(ListView):
    paginate_by = 4
    model = EM
    context_object_name = 'Employers'
    extra_context = {'count': EM.objects.all().count}

# _______________________________________________
# FUNCTIONS    (2)


def Employer_detail(request, slug):
    # Retrieve a specific record by ID
    employer = get_object_or_404(EM, slug=slug)
    jobs=Job.objects.all().filter(employer=employer)
    # Render a template with the record
    return render(request, 'companies/employer_detail.html', {'employer': employer,'jobs':jobs})

# CBV


class EmployerDetail(DetailView):
    model = EM

# ___________________________________________________

# FUNCTIONS    (3)

# def PostJob_choice(request):
#     return render(request,'companies/choice.html',{})
@login_required
def Employer_create(request):
    # Handle form submission for creating a new record
    if request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            employer = form.save()
            employer.user = request.user
            employer.save()
            return HttpResponseRedirect(reverse_lazy('companies:Employer_detail', slug=employer.slug))
    # Render a form for creating a new record
    else:
        form = EmployerForm()
        return render(request, 'companies/employer_create.html', {'form': form})
# CBV


class EmployerCreate(CreateView):
    model = EM
    form_class = EmployerForm
    template_name = 'companies/employer_create.html'
    success_url = reverse_lazy('companies:Employer_detail')
# ___________________________________________________

# FUNCTIONS (4)


def Employer_update(request, slug):
    # Retrieve a specific record by ID
    employer = get_object_or_404(EM, slug=slug)
    # Handle form submission for updating the record
    if request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES, instance=employer)
        if form.is_valid():
            employer = form.save()
            employer.user = request.user
            employer.save()
            return redirect('companies:Employer_detail', slug=employer.slug)
    # Render a form for updating the employer
    else:
        form = EmployerForm(instance=employer)
        return render(request, 'companies/employer_update.html', {'form': form})

# CBV


class EmployerUpdate(UpdateView):
    model = EM
    form_class = EmployerForm
    template_name = 'companies/employer_update.html'
    success_url = reverse_lazy('companies:Employer_list')

# _____________________________________________________

# FUNCTIONS  (5)


def Employer_delete(request, slug):
    # Retrieve a specific record by ID
    employer = get_object_or_404(EM, slug=slug)

    # Handle form submission for deleting the record
    if request.method == 'POST':
        employer.delete()
        return redirect('companies:employer_list')
    # Render a confirmation form for deleting the record
    else:
        return render(request, 'companies/employer_delete.html', {'employer': employer})

# CBV


class EmployerDelete(DeleteView):
    model = EM
    template_name = 'companies/employer_delete.html'
    success_url = reverse_lazy('companies:Employer_list')
