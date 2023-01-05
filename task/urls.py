from django.urls import path
from .views import CreateTaskView, EditTaskView, ListAllTasksView, TaskDetailsView, RedirectToTasksView, DeleteTaskView

app_name = 'task'
urlpatterns = [
    path('', ListAllTasksView.as_view(), name='list-all'),
    path('all', RedirectToTasksView.as_view()),
    path('<int:task_id>/', TaskDetailsView.as_view(), name='details'),
    path('<int:task_id>/edit', EditTaskView.as_view(), name='edit'),
    path('<int:task_id>/delete', DeleteTaskView.as_view(), name='delete'),
    path('new', CreateTaskView.as_view(), name='new')
]
