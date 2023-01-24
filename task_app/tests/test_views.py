from django.test import TestCase
from django.urls import reverse


class TaskListView(TestCase):

    def test_url_exists(self):
        response = self.client.get("/tasks/2")
        self.assertEqual(response.status_code, 200)

