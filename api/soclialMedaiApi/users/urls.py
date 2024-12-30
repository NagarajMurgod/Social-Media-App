from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<int:user_id>/', views.ProfileView.as_view(),name="profile_details"),
    path('profile/<int:followee_id>/follow/', views.FollowView.as_view(), name="follow_user"),
    path('profile/<int:followee_id>/unfollow/', views.UnFollowView.as_view(), name="unfollow_user"),
]