from django.urls import path, include
from .views import ListNotificationView,ClearNotification

urlpatterns = [
    path('<int:id>/', ListNotificationView.as_view(), name = "user_notification"),
    path("clear/",ClearNotification.as_view(), name="clear_notification")
]