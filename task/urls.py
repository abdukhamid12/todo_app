from django.urls import path
from task.views import *

urlpatterns = [
    path('', home, name='home'),
    path('modal_create/', modal_create, name='modal_create')
]