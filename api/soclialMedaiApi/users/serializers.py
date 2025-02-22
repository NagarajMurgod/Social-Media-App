from rest_framework import serializers
from .models import Profile,Follow
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        read_only_fields = ["username"]


class GetUserList(serializers.ModelSerializer):
    profile_img = serializers.ImageField(source="profile.profile_img")
    is_following = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id","username", "profile_img", "is_following"]
    
    def get_is_following(self,obj):
        view = self.context.get("view")
        request = self.context.get("request")
        user_id = view.kwargs.get("user_id")
        
        if not user_id:
            user_id = request.user.id
        # return True
        return Follow.objects.filter(followee__id=user_id,follower=obj).exists()




class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False,required=False)
    followers = serializers.SerializerMethodField(read_only=True)
    following = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile 
        fields = ["bio","profile_img","user","followers","following", "is_following"]
        read_only_fields = ["followers", "following"]

    
    def get_followers(self, obj):
        followers = obj.user.followers.count()
        return  followers
    
    def get_following(self,obj):
        followees = obj.user.followees.count()
        return  followees
    
    def get_is_following(self,obj):
        # view = self.context.get("view")
        request = self.context.get("request")
        # user_id = view.kwargs.get("user_id")
        # return True
        return Follow.objects.filter(followee__id=obj.user.id,follower__id=request.user.id).exists()
        # return Follow.objects.filter(followee__id=user_id,follower=obj).exists()

    
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