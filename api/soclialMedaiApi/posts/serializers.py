from rest_framework import serializers
from .models import Post,Tag,Comment
from authentication.models import User
from users.models import Profile



class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title"]
        extra_kwargs = {
            "title": {
                "validators": []
            }
        }


class PostSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True,required=False)
    comments_count = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username',read_only=True)
    profile_img = serializers.ImageField(source='user.profile.profile_img',read_only=True)

    class Meta:
        model = Post 
        fields = ["id","username", "profile_img", "image", "caption", "like_count", "comments_count", "tags"]
        read_only_fields = ["id", "comments_count","like_count", "username","profile_img"]
    

    def get_comments_count(self, obj):
        comment_count = obj.list_comments.count()
        return comment_count


    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        post_obj = super().create(validated_data)
        for tag in tags:
            tag,created = Tag.objects.get_or_create(title=tag['title'].strip().lower())
            post_obj.tag.add(tag)

        return post_obj


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["id", "user", "post","detail"]
    

    
    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("This post does not exist.")
        return value
