from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import CreateUserSerializer,LoginUserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model,login
from common.helpers import validation_error_handler
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
# Create your views here.

User = get_user_model()


@method_decorator(ensure_csrf_cookie, name='dispatch')
class SetCSRFToken(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        return Response({
            "status" : "success",
            "message" : "CSRF cookie is set",
            "payload" : {}
        })


# @method_decorator(csrf_protect, name='dispatch')
class SignupApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def post(self,request, *args, **kwargs):
        request_data = request.data

        serializer = self.serializer_class(data = request_data)

        if serializer.is_valid() is False:
            return Response({
                "status" : "error",
                "message" : validation_error_handler(serializer.errors),
                "payload" : {
                    "errors" : serializer.errors
                }
            },status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        #email = validated_data.get("email")
        password = validated_data.get("password")
        username = validated_data.get('username')


        user = User.objects.create_user(
            is_active = True,
            **serializer.data
        )

        return Response({
            "status" : "success",
            "message" : "Registration is completed, please login",
            "payload": {}
        })


@method_decorator(csrf_protect, name='dispatch')
class LoginApiView(APIView):
    permission_classes=[AllowAny]
    serializer_class = LoginUserSerializer


    def post(self, request, *args,**kwargs):

        request_data = request.data 
        serializer = self.serializer_class(data = request_data)

        if serializer.is_valid() is False:
            return Response({
                "status" : "error",
                "message" : serializer.errors,
                "payload" : {
                    "errors" : serializer.errors
                }
            })
        
        username_or_email = serializer.validated_data.get("username_or_email")
        password = serializer.validated_data.get("password")

        user = (User.objects.filter(email = username_or_email).first() or User.objects.filter(username = username_or_email).first())

        if user is not None:
            if check_password(password, user.password):
                login(request, user)
                return Response({
                    "status" : "success",
                    "message" : "Login successful",
                    "playload" : {}
                })
            else:
                return Response({
                    "status": "error",
                    "message" : "Username or Password incorrect",
                    "payload" : {}
                })
        else:
            return Response({
                "status" : "error",
                "message" : "User does not exists",
                "payload" : {}
            })

