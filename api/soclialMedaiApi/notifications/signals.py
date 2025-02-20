from django.db.models.signals import post_save
from users.models import Follow
from .helper import create_follow_notification
from django.dispatch import receiver


@receiver(post_save, sender=Follow)
def send_follow_notification(sender, instance, created,**kwargs):
    if created:
        create_follow_notification(follower=instance.follower, followee=instance.followee)