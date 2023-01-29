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

TASK_PER_PAGE = 4


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
        form_errors = []
        row_count = 0
        if not str(tasks_file).endswith('.csv'):
            form_errors.append("CSV file is only supported")
        else:
            lines = TextIOWrapper(tasks_file, encoding="utf-8", newline="")

            for line in DictReader(lines):
                row_count += 1
                form = TaskForm(line)
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


# list tasks by page
@login_required
def list_tasks(request, page):
    tasks = TaskItem.objects.all().order_by("due_date")
    paginator = Paginator(tasks, per_page=TASK_PER_PAGE)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    context = {"page_obj": page_object}
    return render(request, "task_app/index.html", context)


