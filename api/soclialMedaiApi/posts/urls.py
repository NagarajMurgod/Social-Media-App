from django.urls import path, include
from .views import ListCreatePostView


urlpatterns = [
    path("upload/", ListCreatePostView.as_view(),name = "post_upload"),
    path("user_posts/", ListCreatePostView.as_view(),name = "list_post"),
]