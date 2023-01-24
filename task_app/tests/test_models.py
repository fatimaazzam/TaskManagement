from django.test import TestCase
from .models import TaskItem


class ModelsTestCase(TestCase):

    def test_string_method(self):
        task = TaskItem.objects.get(id=1)
        expected_string = f"Name: {task.title} {task.start_date}"
        self.assertEqual(str(task), expected_string)

    def test_get_absolute_url(self):
        task = TaskItem.objects.get(id=1)
        self.assertEqual(task.get_absolute_url(), "/task/1")