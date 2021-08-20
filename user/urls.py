from django.contrib.auth import views as auth
from django.conf.urls import url

from . import views

app_name='user_dashboard'

urlpatterns = [
    url('login',views.user_login, name='login'),
    url('sign_up',views.signup, name='sugnup'),
    url('addlistpost',views.add_list_post, name='addlistpost'),
    url('logout', views.user_logout, name='logout'),
    url('update',views.update_user_post, name='update'),
    url('',views.index, name='home')
]