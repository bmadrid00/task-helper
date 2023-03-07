from django.shortcuts import render
from .models import Project


def list_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "listprojects.html", context)
