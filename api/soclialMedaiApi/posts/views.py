from rest_framework.views import APIView
from .serializers import PostSerializer,CommentSerializer
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Comment,PostLike
import json
from rest_framework.pagination import CursorPagination
from .permissions import IsPostOwner
from rest_framework import viewsets
from django.db.models import Q, Max,Value, F


class PostPagination(CursorPagination):
    page_size = 2  # Number of posts to load per request
    ordering = '-created_at'  # Order by the latest posts

class CommentPagination(CursorPagination):
    page_size = 2  # Number of posts to load per request
    ordering = '-created_at'  # Order by the latest posts


class ListCreatePostView(ListCreateAPIView):
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser]
    pagination_class = PostPagination
    # lookup_field = 'user_id'
    
    def get_queryset(self):
        posts = Post.objects.filter().prefetch_related("tags")
        return posts

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     request_data = request.data
    #     serializer = self.get_serializer(data=request_data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.validated_data['user'] = request.user
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response({
    #         "status" : "success",
    #         "message": "successfully uploaded the post",
    #         "payload" : serializer.data
    #     },status = status.HTTP_201_CREATED)
    

class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = "id"
    permission_classes = [IsPostOwner]


class ManagePostCommentsView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        post = Post.objects.filter(pk = self.kwargs["post_id"]).first()
        if post:
            request.data["post"] = post.id
            return super().create(request, *args, **kwargs)
        else:
            return Response({
                "status" : "Error",
                "message" : "Post does not exists",
                "payload" : {}
            }, status=status.HTTP_404_NOT_FOUND)

    
    def get_queryset(self):
        post = Post.objects.filter(pk=self.kwargs['post_id']).first()
        if post:
            return Comment.objects.filter(post=post)
        return Comment.objects.none() 

    
class PostLikesDislikesView(APIView):
    
    def post(self, request, *args, **kwargs):
        post_id = self.kwargs["post_id"]

        post = Post.objects.filter(
            (Q(user__followers__follower = request.user) | Q(user = request.user)),
            id = post_id
        ).first()

        if post is None:
            return Response({
                "status" : "error",
                "message" : "Post not found",
                "payload" : {}
            }, status=status.HTTP_404_NOT_FOUND)
        
        post_like = PostLike.objects.filter(post=post, user=request.user).first()

        
        if post_like is None:
            PostLike.objects.create( post=post, user = request.user)
            post.like_count = F("like_count") + 1
            post.save()
            is_liked = True
        else:
            post_like.delete()
            if post.like_count > 0:
                post.like_count = F("like_count") - 1
            else:
                post.like_count = 0

            is_liked = False
            post.save()

        post.refresh_from_db() 
        return Response({
            "status" : "success",
            "message" : "",
            "payload" : {
                "is_liked" : is_liked,
                "like_count" : post.like_count
            }
        })
        
            
        