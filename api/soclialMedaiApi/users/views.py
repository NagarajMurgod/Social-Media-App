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
        


class ProfileView(APIView):

    permission_classes = [IsOwnerOfProfile]
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        return GetProfileSerializer


    def patch(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user = self.request.user).first()

        if not profile:
            return Response({
                "status" : "error",
                "message" : "Profile not found",
                "payload" : {}
            },status=status.HTTP_404_NOT_FOUND)
        
        self.serializer_class = self.get_serializer_class()
        serializer = self.serializer_class(profile, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status" : "success",
            "message" : "successfully updated the profile",
            "payload" : serializer.data
        })


    def get(self, request, *args, **kwargs):
        self.serializer_class = self.get_serializer_class()
        profile = Profile.objects.filter(user_id = kwargs["id"]).first()

        if not profile:
            return Response({
                "status" : "error",
                "message" : "user no found",
                "payload" : {}
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(profile)
        return Response({
            "status" : "success",
            "message" : "",
            "payload" : serializer.data
        })