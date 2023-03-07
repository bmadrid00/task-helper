from django.shortcuts import render, redirect
from .forms import CreateTaskForm
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
        context = {
            "form": form,
        }
        return render(request, "create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "mytasks.html", context)
