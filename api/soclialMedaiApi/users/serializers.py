from rest_framework import serializers
from .models import Profile,Follow
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        read_only_fields = ["username"]


class GetUserList(serializers.ModelSerializer):
    ...

class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False,required=False)
    followers = serializers.SerializerMethodField(read_only=True)
    following = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Profile 
        fields = ["bio","profile_img","user","followers","following"]
        read_only_fields = ["followers", "following"]

    
    def get_followers(self, obj):
        followers = obj.user.followers.count()
        return  followers
    
    def get_following(self,obj):
        followees = obj.user.followees.count()
        return  followees
    
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