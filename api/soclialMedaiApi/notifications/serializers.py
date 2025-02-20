from rest_framework import serializers
from notifications.models import FollowNotification


class NotificationSerializer(serializers.ModelSerializer):
    is_read = serializers.BooleanField(read_only=False)
    class Meta:
        model = FollowNotification
        fields = ["id","message","is_read","created_at"]
        read_only_fields = ["id", "message","created_at"]
    