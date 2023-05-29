
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('post/', views.post_new, name='post_new'),
    path('edit/<id>',views.edit_customer),
    path('del/<id>',views.delete_customer),
]