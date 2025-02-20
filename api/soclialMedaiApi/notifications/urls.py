from django.urls import path, include
from .views import ListNotificationView

urlpatterns = [
    path('<int:id>/', ListNotificationView.as_view(), name = "user_notification")
]