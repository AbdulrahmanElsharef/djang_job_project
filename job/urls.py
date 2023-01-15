
from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_jobs),
    path('<slug:job_slug>', views.job_details),
]
