
from django.urls import path
from .views import all_jobs,post_job,job_details,candidates

urlpatterns = [
    path('', all_jobs),
    path('add', post_job, name='add_job'),
    path('candidates', candidates, name='candidates'),
    path('<slug:job_slug>', job_details, name='job_detail'),
    # path('<slug:job_slug>/del', del_job),
]
