from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponseBadRequest, Http404
from django.views.generic import RedirectView, ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GreetForm, TaskForm
from .models import Task
# Create your views here.


def index(request: HttpRequest):
    if request.method == 'GET':
        form = GreetForm()
        return render(request, 'form.html', {'form': form})
    elif request.method == 'POST':
        # initialise form with POST data
        form = GreetForm(request.POST)

        if form.is_valid():
            # extract processed name field value
            name = form.cleaned_data.get('name')
            return render(request, 'index.html', {'name': name})
        else:
            # return the same template with error messages
            return render(request, 'form.html', {'form': form})
    else:
        return HttpResponseBadRequest('Invalid request method')


class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    success_url = reverse_lazy('task:list-all')
    template_name = 'create_task.html'

    def form_valid(self, form):
        # associate the user with task
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListAllTasksView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'list_tasks.html'

    def get_queryset(self):
        # get all the tasks from user back reference
        # https://docs.djangoproject.com/en/4.0/topics/db/queries/#related-objects
        return self.request.user.task_set.all()


class TaskDetailsView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_details.html'
    pk_url_kwarg = 'task_id'

    def get(self, request: HttpRequest, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
        except Http404:
            response = redirect(reverse_lazy('task:list-all'), permanent=True)
        finally:
            return response


class RedirectToTasksView(RedirectView):
    url = reverse_lazy('task:list-all')
    permanent = True


class EditTaskView(LoginRequiredMixin, UpdateView):
    form_class = TaskForm
    pk_url_kwarg = 'task_id'
    template_name = 'edit_task.html'
    success_url = reverse_lazy('task:list-all')
    queryset = Task.objects


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    pk_url_kwarg = 'task_id'
    queryset = Task.objects
    success_url = reverse_lazy('task:list-all')
    template_name = 'delete_task.html'
