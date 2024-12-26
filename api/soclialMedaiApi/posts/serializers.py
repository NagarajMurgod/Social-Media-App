from rest_framework import serializers
from .models import Post,Tag



class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title"]


class UploadPostSerializer(serializers.ModelSerializer):

    tags = TagsSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['user','image', 'caption','like_count','tags']
        read_only_fields = ["user"]
    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        post_obj = super().create(validated_data)
        print("tags", tags)
        for tag in tags:
            tag,created = Tag.objects.get_or_create(title=tag['title'].strip().lower())
            post_obj.tag.add(tag)

        return post_obj