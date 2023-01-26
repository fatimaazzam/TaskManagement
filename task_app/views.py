from django.shortcuts import render
# TaskManagement/task_app/views.py

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from csv import DictReader
from io import TextIOWrapper
from django.views.generic.base import View
from .forms import UploadForm, TaskForm
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemListView, self).dispatch(*args, **kwargs)


class ItemCreate(CreateView):
    model = TaskItem
    fields = [
        "title",
        "description",
        "start_date",
        "due_date",
        ]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemCreate, self).dispatch(*args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemUpdate, self).dispatch(*args, **kwargs)

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["title"] = "Edit item"
        return context


class ItemDelete(DeleteView):
    model = TaskItem

    success_url = reverse_lazy("index")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemDelete, self).dispatch(*args, **kwargs)


class UploadView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, "upload.html", {"form": UploadForm()})

    def post(self, request):
        tasks_file = request.FILES["tasks_file"]
        print("tasks_file",tasks_file)
        form_errors = []
        row_count = 0
        if not str(tasks_file).endswith('.csv'):
            form_errors.append("CSV file is only supported")
        else:
            rows = TextIOWrapper(tasks_file, encoding="utf-8", newline="")

            for row in DictReader(rows):
                row_count += 1
                form = TaskForm(row)
                if not form.is_valid():
                    form_errors = form.errors
                    break

                form.save()
        return render(request, "upload.html",
            {
                "form": UploadForm(),
                "form_errors": form_errors,
                "row_count": row_count,
            }
        )


@login_required
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