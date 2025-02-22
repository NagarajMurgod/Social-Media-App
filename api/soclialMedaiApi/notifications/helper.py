from .models import FollowNotification


def create_follow_notification(follower, followee):

    message = f"{follower.username}, started following you!"

    FollowNotification.objects.get_or_create(
        user = followee,
        message = message,
    )
    