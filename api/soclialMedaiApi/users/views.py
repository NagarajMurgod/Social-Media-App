from django.shortcuts import render
from rest_framework.views import APIView
from .models import Follow
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import GetProfileSerializer,GetUserList
from .models import Profile,Follow
from .permissions import IsOwnerOfProfile
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

User = get_user_model()


class FollowView(APIView):
    def post(self, request, *args, **kwargs):
        followee_id = kwargs["followee_id"]
        
        if request.user.id == followee_id:
            return Response({
                "status" : "Success",
                "message" : "You can't follow or unfollow yourself",
                "payload" : {}
            },status=status.HTTP_400_BAD_REQUEST)
        
        if not Follow.objects.filter(follower=request.user, followee_id = followee_id).exists():
            followee = User.objects.filter(id = followee_id).first()
            if followee:
                Follow.objects.create(
                    followee=followee,
                    follower=request.user
                )
            else:
                return Response({
                    "status" : "error",
                    "message": "User does not exists",
                    "payload" : {}
                },status=status.HTTP_404_NOT_FOUND)

        return Response({
            "status" : "success",
            "message": "",
            "payload": {
                "following" : True
            }
        })


class UnFollowView(APIView):

    def post(self, request, *args, **kwargs):
        followee_id = kwargs["followee_id"]
        
        if request.user.id == followee_id:
            return Response({
                "status" : "error",
                "message" : "You can't follow or unfollow yourself",
                "payload" : {}
            },status=status.HTTP_400_BAD_REQUEST)
        
        obj = Follow.objects.filter(follower=request.user, followee_id = followee_id).first()
        if obj:
            obj.delete()

        return Response({
            "status" : "success",
            "message": "",
            "payload": {
                "following" : False
            }
        })
        

class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOfProfile]
    parser_classes = [MultiPartParser]
    serializer_class = GetProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user_id'


class GetUserList(ListAPIView):
    serializer_class = GetUserList
    
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        typ = self.request.query_params.get("type")
       
        if user_id:
            user = get_object_or_404(User, id = user_id)
            if typ == "followers":
                return User.objects.filter(followees__followee = user).select_related("profile").exclude(id=user.id)
            elif typ == "following":
                return User.objects.filter(followers__follower = user).select_related("profile").exclude(id=user.id)
            else:
                return Follow.objects.none()
        return User.objects.prefetch_related(Prefetch("followers", queryset=Follow.objects.filter(followee=self.request.user))).select_related("profile").exclude(id=self.request.user.id)
        