from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^registration/$', views.registration, name = 'registration'),
    url(r'^login/$', login, {'template_name' : 'busterapp/login.jinja'}),
    url(r'^logout/$', logout, {'template_name': 'busterapp/logout.jinja'}),
    url(r'^project/$', views.project, name = 'project'),
    url(r'^project/update_project/(?P<project_id>[0-9]+)/$', views.update_project, name = 'update_project'),
    url(r'^task/$', views.task, name = 'task'),
    url(r'^task/update_task/(?P<task_id>[0-9]+)/$', views.update_task, name = 'update_task'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^(?P<parent_id>[0-9]+)/taskchild/$', views.taskchild, name = 'taskchild'),
]
