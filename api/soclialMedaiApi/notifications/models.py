from django.db import models
from common.models import TimeStampedModel
from django.contrib.auth import get_user_model


User = get_user_model()

class FollowNotification(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"



