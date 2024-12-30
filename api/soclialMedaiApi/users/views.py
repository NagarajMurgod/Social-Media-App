from django.shortcuts import render
from rest_framework.views import APIView
from .models import Follow
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import GetProfileSerializer
from .models import Profile
from .permissions import IsOwnerOfProfile
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView


User = get_user_model()

class FollowView(APIView):

    def post(self, request, *args, **kwargs):
        followee_id = kwargs["followee_id"]
        
        if request.user.id == followee_id:
            return Response({
                "status" : "Success",
                "message" : "You can't follow yourself",
                "payload" : {}
            },status=status.HTTP_400_BAD_REQUEST)
        
        if Follow.objects.filter(follower=request.user, followee_id = followee_id).exists():
            return Response({
                "status" : "success",
                "message": "",
                "payload": {
                    "following" : True
                }
            })
        else:
            followee = User.objects.filter(id = followee_id).first()

            if followee:
                Follow.objects.create(
                    followee=followee,
                    follower=request.user
                )
                return Response({
                    "status" : "success",
                    "message": "",
                    "payload": {
                        "following" : True
                    }
                })
            else:
                return Response({
                    "status" : "error",
                    "message": "User does not exists",
                    "payload" : {}
                },status=status.HTTP_404_NOT_FOUND)


class UnFollowView(APIView):

    def post(self, request, *args, **kwargs):
        followee_id = kwargs["followee_id"]
        
        if request.user.id == followee_id:
            return Response({
                "status" : "error",
                "message" : "You can't unfollow yourself",
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
