from django.shortcuts import render

# TaskManagement/task_app/views.py
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
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


def listing(request, page):
    tasks = TaskItem.objects.all().order_by("due_date")
    paginator = Paginator(tasks, per_page=4)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    context = {"page_obj": page_object}
    return render(request, "task_app/index.html", context)


def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 2)
    startswith = request.GET.get("startswith", "")
    tasks = TaskItem.objects.filter(
        title__startswith=startswith
    )
    paginator = Paginator(tasks, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"title": task.title} for task in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)