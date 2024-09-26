from django.urls import path
from . import views

app_name="Lyf_Logs"
urlpatterns = [
    path("", views.lyf, name="Lyf"),
    path("add/", views.add, name="add"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("view/<int:id>/", views.view, name="view"),
]