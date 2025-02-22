from rest_framework import serializers
from notifications.models import FollowNotification


class NotificationSerializer(serializers.ModelSerializer):
    is_read = serializers.BooleanField(read_only=False)
    class Meta:
        model = FollowNotification
        fields = ["id","message","is_read","created_at"]
        read_only_fields = ["id", "message","created_at"]
    
    # def to_representation(self,instance):
    #     representation = super().to_representation(instance)
    #     user = self.context["request"].user
    #     cnt =  FollowNotification.objects.filter(user=user).count()
    #     representation["read_count"] = cnt
    #     return representation

        