from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Task
from django.contrib import messages


def index(request: HttpRequest) -> HttpResponse:
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(is_deleted=False)

    context = {"tasks": tasks}

    return render(request, "tasks/index.html", context)


def add(request: HttpRequest) -> HttpResponse:
    if request.POST:
        task = Task()
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.save()

        messages.success(request, "創建成功")

        # 繼續待在新增頁面，可以進行下一筆任務新增
        return redirect("tasks:add")

    return render(request, "tasks/add.html")


def detail(request: HttpRequest, id: int) -> HttpResponse:
    task = get_object_or_404(Task, id=id)
    context = {"task": task}

    return render(request, "tasks/detail.html", context)


def edit(request: HttpRequest, id: int) -> HttpResponse:
    task = get_object_or_404(Task, id=id)
    context = {"task": task}

    if request.POST:
        task.title = request.POST.get("title", task.title)
        task.description = request.POST.get("description", task.description)
        task.save()

        messages.success(request, "更新成功")
        return redirect("tasks:detail", id=task.id)

    return render(request, "tasks/edit.html", context)


def delete(request: HttpRequest, id: int) -> HttpResponse:
    if request.POST:
        task = get_object_or_404(Task, id=id)

        task.is_deleted = True
        task.save()
        # task.delete()

        messages.success(request, "刪除成功")

        return redirect("tasks:index")
