from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user = self.request.user)

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__incotains=search_input)
        context["search_input"] = search_input
        return context
class TaskCreate():
    model = Task
    fields = ["title","description","complete"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)