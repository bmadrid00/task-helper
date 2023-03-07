from django.urls import path
from .views import login_view, logout_view, sign_up_view


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", sign_up_view, name="signup"),
]
