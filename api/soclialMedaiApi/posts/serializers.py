from rest_framework import serializers
from .models import Post,Tag,Comment



class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title"]
        extra_kwargs = {
            "title": {
                "validators": []
            }
        }


class UploadPostSerializer(serializers.ModelSerializer):

    tags = TagsSerializer(many=True,required=False)

    class Meta:
        model = Post
        fields = ['user','image', 'caption','like_count','tags']
        read_only_fields = ["user"]

    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        post_obj = super().create(validated_data)
        for tag in tags:
            tag,created = Tag.objects.get_or_create(title=tag['title'].strip().lower())
            post_obj.tag.add(tag)

        return post_obj


class PostSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post 
        fields = ["id","image", "caption", "like_count", "comments_count", "tags"]

    
    def get_comments_count(self, obj):
        comment_count = Comment.objects.filter(post=obj).count()
        return comment_count



class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["id", "user", "post","detail"]
    

    
    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("This post does not exist.")
        return value
