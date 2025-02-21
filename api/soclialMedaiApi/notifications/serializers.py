from rest_framework import serializers
from notifications.models import FollowNotification


class NotificationSerializer(serializers.ModelSerializer):
    is_read = serializers.BooleanField(read_only=False)
    count = serializers.SerializerMethodField()
    class Meta:
        model = FollowNotification
        fields = ["id","message","is_read","created_at","count"]
        read_only_fields = ["id", "message","created_at","count"]
    
    def get_count(self, obj):
        user = self.context["request"].user
        return FollowNotification.objects.filter(user=user).count()