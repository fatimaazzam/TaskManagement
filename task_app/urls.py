from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.ItemListView.as_view(), name="index"),
    path("task/add/", views.ItemCreate.as_view(), name="task-add"),
    path("task/<int:pk>/", views.ItemUpdate.as_view(), name="item-update", ),
    path("task/<int:pk>/delete/", views.ItemDelete.as_view(), name="task-delete"),
    path("tasks/<int:page>", views.listing, name="task-by-page"),
    path("task.json", views.listing_api, name="task-api"),
]