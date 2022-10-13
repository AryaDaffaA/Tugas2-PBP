# TODO: Implement Routings Here
from django.urls import path
from todolist.views import todoList
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import add_task_ajax
from todolist.views import show_json
from todolist.views import show_ajax

app_name = 'todolist'

urlpatterns = [
    path('', todoList, name = 'todoList'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtask/', add_task, name='add_task'),
    path('json/', show_ajax, name='show_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax'),
    path('show-json/', show_json, name='show_json')
]