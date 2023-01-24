from django.shortcuts import render

# TaskManagement/task_app/views.py
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
)
from django.urls import reverse_lazy
from .models import TaskItem


class ItemListView(ListView):
    model = TaskItem
    template_name = "task_app/index.html"


class ItemCreate(CreateView):
    model = TaskItem
    fields = [
        "title",
        "description",
        "start_date",
        "due_date",
        ]

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        context["title"] = "Add a new task"
        return context


class ItemUpdate(UpdateView):
    model = TaskItem
    fields = [
        "title",
        "description",
        "start_date",
        "due_date",
        ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["title"] = "Edit item"
        return context


class ItemDelete(DeleteView):
    model = TaskItem

    success_url = reverse_lazy("index")
