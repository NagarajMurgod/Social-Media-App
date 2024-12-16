from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignupApiView.as_view(), name="signup"),
    path("login/", views.LoginApiView.as_view(), name="login")
]