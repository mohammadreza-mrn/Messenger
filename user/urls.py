


from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("auth",views.AuthenticateView.as_view(),name="auth-view"),
    path("register",views.RegisterView.as_view(),name="register-view")
]