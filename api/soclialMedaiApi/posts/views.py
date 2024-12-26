from rest_framework.views import APIView
from .serializers import UploadPostSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status


class UploadPostView(ListCreateAPIView):
    serializer_class = UploadPostSerializer
    parser_classes = [MultiPartParser]

    def create(self, request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        serializer.save()

        return Response({
            "status" : "success",
            "message": "successfully uploaded the post",
            "payload" : serializer.data
        },status = status.HTTP_201_CREATED)