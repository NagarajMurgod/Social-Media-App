from rest_framework.views import APIView
from .serializers import PostSerializer,CommentSerializer
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Comment,PostLike
import json
from rest_framework.pagination import CursorPagination
from django.shortcuts import get_object_or_404
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
    
    def get_queryset(self):
        
        if self.kwargs.get('id'):
            queryset = Post.objects.filter(user_id = self.kwargs.get('id')).prefetch_related("tags","user","user__profile")
        else:
            queryset = Post.objects.all().prefetch_related("tags")
        
        return queryset


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = "id"
    permission_classes = [IsPostOwner]


class ManagePostCommentsView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    def perform_create(self,serializer):
        post = get_object_or_404(Post , pk = self.kwargs["post_id"])
        serializer.save(post=post, user = self.request.user)
    
    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        if post:
            return Comment.objects.filter(post=post).prefetch_related("user","user__profile")
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
        
            
        