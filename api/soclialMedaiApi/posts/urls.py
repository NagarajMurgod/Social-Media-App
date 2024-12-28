from django.urls import path, include
from .views import ListCreatePostView,DeletePostView,ManagePostCommentsView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'(?P<post_id>\d+)/comments', ManagePostCommentsView, basename='post_comments')

urlpatterns = [
    path('', include(router.urls)),
    path("upload/", ListCreatePostView.as_view(),name = "post_upload"),
    path("user_posts/", ListCreatePostView.as_view(),name = "list_post"),
    path("<int:id>/",DeletePostView.as_view(), name="delete_post")
]