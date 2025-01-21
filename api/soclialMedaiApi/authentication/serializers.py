from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User 
        fields = [ "username", "email", "password", "confirm_password"]


    def validate(self,attrs):
        password = attrs.get('password')
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Password must match")
        return attrs
    

    def validate_email(self,value):
        email = value.lower()
        return email


    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username is already exisits")
        return value


class LoginUserSerializer(serializers.ModelSerializer):
    username_or_email = serializers.CharField(write_only=True)
    profile_img = serializers.ImageField(source='profile.profile_img',read_only=True)
    class Meta:
        model = User 

        fields = [
            "username_or_email",
            "email",
            "password",
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "profile_img"
        ]

        read_only_fields = [
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "profile_img"
        ]

        extra_kwargs = {
            "password" : { "write_only" : True},
            "email" : {"write_only": True}
        }

        def validate_username_or_email(self,value):
            return value.lower()


