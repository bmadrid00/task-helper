from django.shortcuts import render, redirect
from .forms import CreateTaskForm
from django.contrib.auth.decorators import login_required


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
