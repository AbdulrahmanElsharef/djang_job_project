from django.urls import path
from companies.views import Employer_list, Employer_create, Employer_detail, Employer_update, Employer_delete
from companies.views import EmployerList, EmployerCreate, EmployerUpdate, EmployerDetail, EmployerDelete

app_name = 'companies'

urlpatterns = [
    path('Employers/', Employer_list, name='employer_list'),  # functions
    # path('Employers/', EmployerList.as_view() ,name='Employer_list'), #cbv
    path('Employers/create', Employer_create,
         name='Employer_create'),  # functions
    # path('Employers/create', EmployerCreate.as_view() ,name='Employer_create'),# cbv
    path('Employers/<slug:slug>', Employer_detail,
         name='Employer_detail'),  # functions
    # path('Employers/<slug:slug>', EmployerDetail.as_view() ,name='Employer_detail'), #cbv
    path('Employers/<slug:slug>/update', Employer_update,
         name='Employer_update'),  # functions
    # path('Employers/<slug:slug>/update', EmployerUpdate.as_view() ,name='Employer_update'), #cbv
    path('Employers/<slug:slug>/del', Employer_delete,
         name='Employer_delete'),  # functions
    # path('Employers/<slug:slug>/del', EmployerDelete.as_view() ,name='Employer_delete'), #cbv
]
