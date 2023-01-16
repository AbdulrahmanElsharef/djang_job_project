
from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_jobs),
    path('<slug:job_slug>', views.job_details),
    path('<slug:job_slug>/edit', views.Edit_job),
    path('<slug:job_slug>/del', views.del_job),
]
