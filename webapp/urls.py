from django.urls import path
from webapp.views import task_list_view,task_detail_view,task_create_view, task_update_view, task_delete_view


urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('task/<int:pk>/', task_detail_view, name='task_detail'),
    path('task/create/', task_create_view, name='task_create'),
    path('task/<int:pk>/update/', task_update_view, name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete'),

]