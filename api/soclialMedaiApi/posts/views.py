from rest_framework.views import APIView
from .serializers import UploadPostSerializer,PostSerializer
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Post
import json
from rest_framework.pagination import CursorPagination
from .permissions import IsPostOwner


class PostPagination(CursorPagination):
    page_size = 2  # Number of posts to load per request
    ordering = '-created_at'  # Order by the latest posts


class ListCreatePostView(ListCreateAPIView):
    # serializer_class = UploadPostSerializer
    parser_classes = [MultiPartParser]
    pagination_class = PostPagination

    def get_queryset(self):
        posts = Post.objects.filter().prefetch_related("tags")
        return posts


    def get_serializer_class(self):
        if self.request and self.request.method == "POST":
            return UploadPostSerializer
        return PostSerializer


    def create(self, request, *args, **kwargs):
        request_data = request.data
        tags = request_data["tags"]
        request_data["tags"] = json.loads(tags)
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        serializer.save()

        return Response({
            "status" : "success",
            "message": "successfully uploaded the post",
            "payload" : serializer.data
        },status = status.HTTP_201_CREATED)
    

class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = "id"
    permission_classes = [IsPostOwner]