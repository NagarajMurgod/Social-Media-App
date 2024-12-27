from django.urls import path, include
from .views import ListCreatePostView,DeletePostView


urlpatterns = [
    path("upload/", ListCreatePostView.as_view(),name = "post_upload"),
    path("user_posts/", ListCreatePostView.as_view(),name = "list_post"),
    path("<int:id>/",DeletePostView.as_view(), name="delete_post")
]