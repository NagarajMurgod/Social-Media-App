from rest_framework import serializers
from .models import Profile
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        read_only = ["username"]



class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False)
    class Meta:
        model = Profile 
        fields = ["bio","profile_img","user"]
    
    def update(self,instance, validate_data):
        profile_img = validate_data.get("profile_img", None)

        if profile_img:
            if instance.profile_img:
                instance.profile_img.delete()
            instance.profile_img = profile_img
        
        user_data = validate_data.get("user",None)
        if user_data:
            user_instance = instance.user 
            user_instance.first_name = user_data.get("first_name", user_instance.first_name)
            user_instance.last_name = user_data.get("last_name", user_instance.last_name)
            user_instance.save()

        instance.bio = validate_data.get("bio", instance.bio)
        instance.save()
        return instance