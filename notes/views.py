from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Note
from django.urls import reverse_lazy
from django.contrib import messages


# 舊的 note 首頁
class NoteIndexView(TemplateView):
    template_name = "notes/index.html"


# 新的 note 首頁
class NoteListView(ListView):
    template_name = "notes/index.html"
    model = Note
    context_object_name = "notes"


class NoteCreateView(CreateView):
    template_name = "notes/add.html"
    model = Note
    fields = ["title", "description"]
    success_url = reverse_lazy("notes:add")

    def form_valid(self, form):
        messages.success(self.request, "創建成功")
        return super().form_valid(form)


class NoteDetailView(DetailView):
    template_name = "notes/detail.html"
    model = Note
    context_object_name = "note"


class NoteUpdateView(UpdateView):
    template_name = "notes/edit.html"
    fields = ["title", "description"]
    model = Note
    context_object_name = "note"

    def get_success_url(self):
        return reverse_lazy("notes:detail", kwargs={"pk": self.object.id})

    def form_valid(self, form):
        messages.success(self.request, "更新成功")
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    context_object_name = "note"
    success_url = reverse_lazy("notes:index")
