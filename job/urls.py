
from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_jobs),
    path('<int:job_id>', views.job_details),
]
