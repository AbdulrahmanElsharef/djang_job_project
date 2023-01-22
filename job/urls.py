
from django.urls import path
from .views import all_jobs,post_job, job_details, del_job

urlpatterns = [
    path('jobs', all_jobs),
    path('jobs/add', post_job),
    path('jobs/<slug:job_slug>', job_details),
    # path('jobs/<slug:job_slug>/edit', Edit_job),
    path('jobs/<slug:job_slug>/del', del_job),
]
