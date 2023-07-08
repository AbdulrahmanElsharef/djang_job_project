from django.urls import path
# from .views import Job_list,Job_create,Job_detail,Job_update,Job_delete
from .views import JobList,JobCreate,JobUpdate,JobDetail,JobDelete

app_name='board'

urlpatterns = [
    # path('jobs/', Job_list ,name='job_list'),  #functions
    path('jobs/', JobList.as_view() ,name='job_list'), #cbv
    # path('jobs/create', Job_create ,name='job_create') ,  #functions
    path('jobs/create', JobCreate.as_view() ,name='job_create'),# cbv
    # path('jobs/<slug:slug>', Job_detail ,name='job_detail'),  #functions
    path('jobs/<slug:slug>', JobDetail.as_view() ,name='job_detail'), #cbv
    # path('jobs/<slug:slug>/update', Job_update ,name='job_update'), # functions
    path('jobs/<slug:slug>/update', JobUpdate.as_view() ,name='job_update'), #cbv
    # path('jobs/<slug:slug>/del', Job_delete ,name='job_delete'),  #functions
    path('jobs/<slug:slug>/del', JobDelete.as_view() ,name='job_delete'), #cbv

]