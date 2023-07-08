from django.urls import path
# from blog.views import Post_list,Post_create,Post_detail,Post_update,Post_delete
from blog.views import PostList,PostAdd,PostUpdate,PostDetail,PostDelete

app_name='blog'

urlpatterns = [
    # path('posts/', Post_list ,name='post_list'),  #functions
    path('posts/', PostList.as_view() ,name='post_list'), #cbv
    # path('posts/create', Post_create ,name='post_create') ,  #functions
    path('posts/add', PostAdd.as_view() ,name='post_add'),# cbv
    # path('posts/<slug:slug>', Post_detail ,name='post_detail'),  #functions
    path('posts/<slug:slug>', PostDetail.as_view() ,name='post_detail'), #cbv
    # path('posts/<slug:slug>/update', Post_update ,name='post_update'), # functions
    path('posts/<slug:slug>/update', PostUpdate.as_view() ,name='post_update'), #cbv
    # path('posts/<slug:slug>/del', Post_delete ,name='post_delete'),  #functions
    path('posts/<slug:slug>/del', PostDelete.as_view() ,name='post_delete'), #cbv
]