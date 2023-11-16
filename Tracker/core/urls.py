from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
