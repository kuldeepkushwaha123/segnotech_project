
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('postComment',views.postComment,name="postComment"),
    
    path('',views.bloghome,name='bloghome'),
    path('<str:slug>/',views.blogpost,name='blogpost'),
    

    # path('', views.home,name='home'),
    # path('index/', views.index,name='index'),
    # path('post/', views.post_new, name='post_new'),
    # path('edit/<slug>',views.edit_customer),
    # path('del/<slug>',views.delete_customer),
    
    #
    # path('postcomment',views.postComment,name = 'postcomment')

]