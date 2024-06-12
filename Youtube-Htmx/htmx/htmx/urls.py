from django.contrib import admin
from django.urls import path
from Apphtmx.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("todo_add/", todo_add, name="todo_add"),
    path("todo_update/<int:todo_id>", todo_update, name="todo_update"),
    path("todo_delete/<int:todo_id>", todo_delete, name="todo_delete"),
]
