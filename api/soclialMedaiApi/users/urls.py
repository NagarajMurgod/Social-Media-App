from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<int:id>/', views.ProfileView.as_view(),name="profile_details"),
]