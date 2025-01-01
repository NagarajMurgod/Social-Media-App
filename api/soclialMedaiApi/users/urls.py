from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<int:user_id>/', views.ProfileView.as_view(),name="profile_details"),
    path('profile/follow/<int:followee_id>/', views.FollowView.as_view(), name="follow_user"),
    path('profile/unfollow/<int:followee_id>/', views.UnFollowView.as_view(), name="unfollow_user"),
    path('profile/<int:user_id>/relations/',views.GetUserList.as_view(), name="followers_unfollowers_details"),
    path('list/',views.GetUserList.as_view(), name="followers_unfollowers_details")
]