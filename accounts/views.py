from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)
    else:
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def sign_up_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username=username, password=password
                )
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error("password", "the passwords do not match")
    else:
        form = SignUpForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/signup.html", context)
