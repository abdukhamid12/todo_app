from django.urls import path
from task.views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('task-done-view/', task_done_view, name='task_done_view'),
    path('task-deleted-view/', task_delete_view, name='task_delete_view'),
    path('done-deleted-task-view/', done_delete_task_view, name='done_deleted_task_view'),

    path('search/', search, name='search-task'),

    path('create-task/', create_task, name='create-task'),

    path('edit-task/', edit_task, name='edit_task'),
    path('delete-task/', delete_task, name='delete_task'),
]