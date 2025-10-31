from django.urls import path
from webapp.views import task_list_view,task_detail_view,task_create_view


urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('task/<int:pk>/', task_detail_view, name='task_detail'),
    path('task/create/', task_create_view, name='task_create'),
]