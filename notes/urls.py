from django.urls import path
from .views import (
    NoteIndexView,
    NoteCreateView,
    NoteListView,
    NoteDetailView,
    NoteUpdateView,
    NoteDeleteView,
)

app_name = "notes"

urlpatterns = [
    path("", NoteListView.as_view(), name="index"),
    path("add/", NoteCreateView.as_view(), name="add"),
    path("<int:pk>/detail/", NoteDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", NoteUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="delete"),
]
