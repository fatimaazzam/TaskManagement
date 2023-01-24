from django.forms import FileField, Form, ModelForm

from .models import TaskItem


class TaskForm(ModelForm):
    class Meta:
        model = TaskItem
        fields = ["title", "start_date", "due_date", "description"]


class UploadForm(Form):
    tasks_file = FileField()